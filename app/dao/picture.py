from ..util import get_connection
import os
import json
import urllib
import subprocess

class Picture:
    def __init__(self):
        self.conn = get_connection.setup()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def all(self):
        sql = """
            SELECT p.id, p.title, p.description, p.path,
                p.position, c.name as "category", p.category_id
            FROM picture p JOIN category c
            ON p.category_id = c.id
            ORDER BY category, p.position
            """
        self.cursor.execute(sql)
        pics = self.cursor.fetchall()
        return pics

    def by_category(self, category_id):
        sql = """
            SELECT p.id, p.title, p.description, p.path,
                p.position, c.name as "category", p.category_id
            FROM picture p JOIN category c
            ON p.category_id = c.id
            WHERE p.category_id = ?
            ORDER BY category, p.position
            """
        self.cursor.execute(sql, [category_id])
        return self.cursor.fetchall()

    def by_category_name(self, name):
        sql = """
            SELECT p.id, p.title, p.description, p.path,
                p.position, c.name as "category", p.category_id
            FROM picture p JOIN category c
            ON p.category_id = c.id
            WHERE c.name = ?
            ORDER BY category, p.position
            """
        self.cursor.execute(sql, [name])
        return self.cursor.fetchall()
        

    def by_category_position(self, category_position):
        sql = "SELECT id FROM category WHERE position = ?"
        self.cursor.execute(sql, [int(category_position)])
        category = self.cursor.fetchone()
        sql = """
            SELECT p.id, p.title, p.description, p.path,
                p.position, c.name as "category", p.category_id
            FROM picture p JOIN category c
            ON p.category_id = c.id
            WHERE p.category_id = ?
            ORDER BY category, p.position
            """
        self.cursor.execute(sql, [category['id']])
        return self.cursor.fetchall()

    def by_picture_position_category_position(self, picture_position, category_position):
        sql = """
            SELECT p.id, p.title, p.description, p.path,
                p.position, c.name as "category", p.category_id
            FROM picture p JOIN category c
            ON p.category_id = c.id
            WHERE p.position = ? AND c.position = ? 
            """
        self.cursor.execute(sql, (int(picture_position), int(category_position)))
        return self.cursor.fetchone()

    def by_id(self, id):
        sql = """
            SELECT p.id, p.title, p.description, p.path,
                p.position, c.name as "category", p.category_id
            FROM picture p JOIN category c
            ON p.category_id = c.id
            WHERE p.id = ?
            """
        self.cursor.execute(sql, [id])
        return self.cursor.fetchone()

    def insert(self, data):
        assert['picture'] != ""
        sql = 'SELECT MAX(position) AS "position" FROM picture WHERE category_id = ?'
        self.cursor.execute(sql, (data['category_id'],))
        position = self.cursor.fetchone()['position']
        if position == None:
            position = 0
        position = position + 1
        sql = """
            INSERT INTO picture(`title`, `description`, `position`, `category_id`)
            VALUES( ?, ?, ?, ?)
            """
        self.cursor.execute(sql, (data['title'], data['description'], str(position),
            data['category_id']))
        sql = "SELECT MAX (id) AS 'id' FROM picture"
        self.cursor.execute(sql)
        id = str(self.cursor.fetchone()['id'])
        fn, ext = os.path.splitext(data['picture'].filename)
        picture_path = 'assets/picture'+id+ext
        print picture_path
        open(picture_path, 'wb').write(data['picture'].file.read())
        subprocess.call(['convert', 'assets/picture'+id+ext, '-resize', 'x630', 'assets/picture'+id+'res'+ext])
        subprocess.call(['convert', picture_path, '-resize', 'x50', 'assets/picture'+id+'thumb'+ext])
        sql = "UPDATE picture SET path = ? WHERE id = ?"
        self.cursor.execute(sql, (picture_path, id))

    def update(self, data):
        sql = """
            UPDATE picture SET title = ?, description = ?, category_id = ?
            WHERE id = ?
            """
        self.cursor.execute(sql, (data['title'], data['description'], data['category_id'],
            data['id']))
        if data['picture'] != "":
            fn, ext = os.path.splitext(data['picture'].filename)
            picture_path = 'assets/picture'+data['id']+ext
            open(picture_path, 'wb').write(data['picture'].file.read())
            subprocess.call(['convert', picture_path, '-resize', 'x630', 'assets/picture'+data['id']+'res'+ext])
            subprocess.call(['convert', picture_path, '-resize', 'x50', 'assets/picture'+data['id']+'thumb'+ext])

    def update_position(self, id, position):
        sql = "UPDATE picture SET position = ? WHERE id = ?"
        self.cursor.execute(sql, (position, id))

    def delete(self, id):
        sql = "SELECT category_id, path FROM picture WHERE id = ?"
        self.cursor.execute(sql, [id])
        pic = self.cursor.fetchone()
        path = pic['path']
        fn, ext = os.path.splitext(path)
        os.unlink('assets/picture'+id+''+ext)
        os.unlink('assets/picture'+id+'res'+ext)
        os.unlink('assets/picture'+id+'thumb'+ext)
        category_id = pic['category_id']
        sql = "DELETE FROM picture WHERE id = ?"
        self.cursor.execute(sql, [id])
        self.conn.commit()
        self.rearrange_position(category_id)

    def rearrange_position(self, category_id):
        pics = self.by_category(category_id) 
        i = 1
        for pic in pics:
            self.update_position(pic['id'], i)
            i = i + 1
