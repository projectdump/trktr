from ..util import get_connection
import os

class Text:
    def __init__(self):
        self.conn = get_connection.setup()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def all(self):
        sql = """
            SELECT t.id, t.name, t.content, t.position,
                c.name as "category", t.category_id, t.abstract, t.home
                t.size, t.overlap, t.format, t.coverpic, t.alignment
            FROM text t JOIN category c
            ON t.category_id = c.id
            ORDER BY category, t.position
            """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_names():
        sql = "SELECT name FROM text ORDER BY position"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def by_id(self, id):
        sql = """
            SELECT t.id, t.name, t.content, t.position,
                c.name as "category", t.category_id, t.abstract ,
                t.home, t.footer, t.sidebar,
                t.size, t.overlap, t.format, t.coverpic, t.alignment
            FROM text t JOIN category c
            ON t.category_id = c.id
            WHERE t.id = ?
            ORDER BY category, t.position
            """
        self.cursor.execute(sql, [id])
        return self.cursor.fetchone()

    def by_category(self, id):
        sql = """
            SELECT t.id, t.name, t.content, t.position,
                c.name as "category", t.category_id, t.abstract, t.home,
                t.footer as "footer", t.sidebar,
                t.size, t.overlap, t.format, t.coverpic, t.alignment
            FROM text t JOIN category c
            ON t.category_id = c.id
            WHERE t.category_id = ?
            ORDER BY category, t.position
            """
        self.cursor.execute(sql, [id])
        return self.cursor.fetchall()
            
    def by_position(self, position):
        sql = """
            SELECT t.id, t.name, t.content, t.position,
                c.name as "category", t.category_id, t.abstract,
                t.size, t.overlap, t.format, t.coverpic, t.alignment
            FROM text t JOIN category c
            ON t.category_id = c.id
            WHERE t.position = ?
            ORDER BY category, t.position
            """
        self.cursor.execute(sql, [int(position)])
        return self.cursor.fetchone()

    def get_metas(self):
        sql = """
            SELECT t.id, t.name, t.content, t.position,
                c.name as "category", t.category_id, t.abstract,
                t.home, t.footer, t.sidebar,
                t.size, t.overlap, t.format, t.coverpic, t.alignment
            FROM text t JOIN category c
            ON t.category_id = c.id
            ORDER BY t.category_id, t.position
            """
        self.cursor.execute(sql)
        return  self.cursor.fetchall()

    def insert(self, data):
        sql = """
            SELECT MAX(t.position) AS "position"
            FROM text t JOIN category c
            ON t.category_id = c.id
            WHERE c.id = ?
            """
        self.cursor.execute(sql, [data['category_id']])
        position = self.cursor.fetchone()['position']
        if position == None:
            position = 0;
        position = position + 1
        coverpicpath = "assets/default_coverpic.png"
        if data['coverpic'] != "":
            coverpicpath = self.coverpic(data)
        sql = """
            INSERT INTO text(`name`, `content`,
            `position`, `category_id`, `abstract`, `alignment`, `overlap`,
            `size`, `format`, `coverpic`) 
            VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
        self.cursor.execute(sql, (data['name'], 
            data['content'], 
            str(position),
            data['category_id'],
            data['abstract'],
            data['alignment'],
            data['overlap'],
            data['size'],
            data['format'],
            coverpicpath))

    def coverpic(self, data):
        fn, ext = os.path.splitext(data['coverpic'].filename)
        picture_path = 'assets/'+data['name']+'_coverpic'+ext
        picture_path = picture_path.replace(" ", "-")
        open(picture_path, 'wb').write(data['coverpic'].file.read())
        return picture_path

    def update(self, data):
        sql = """
            UPDATE text SET name = ?, content = ?,
                category_id = ?, abstract = ?,
                alignment= ?, overlap = ?, size = ?,
                format = ?
            WHERE id = ?
            """
        self.cursor.execute(sql, (data['name'], data['content'],  data['category_id'], data['abstract'], data['alignment'], data['overlap'], data['size'], data['format'], data['id']))
        if data['coverpic'] != "":
            sql = """SELECT coverpic FROM text WHERE id = ?"""
            self.cursor.execute(sql, (data['id'],))
            t = self.cursor.fetchone()
            try: 
                os.unlink(t['coverpic'])
            except OSError:
                print OSError
            coverpicpath = self.coverpic(data)
            print coverpicpath
            sql = "UPDATE text SET coverpic = ? WHERE id = ?"
            self.cursor.execute(sql, (coverpicpath, data['id']))

    def update_position(self, id, position):
        sql = "UPDATE text SET position = ? WHERE id = ?"
        self.cursor.execute(sql, (position, id))

    def delete(self, id):
        sql = "DELETE FROM text WHERE id = ?"
        self.cursor.execute(sql, [id])

    def by_top_menu(self):
        sql = """
            SELECT t.id, t.name, t.content, t.position,
                c.name as "category", t.category_id, t.abstract
            FROM text t JOIN category c
            ON t.category_id = c.id
            WHERE t.menu = 0
            ORDER BY category, t.position
            """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def search(self, string):
        sql = """
            SELECT t.name as "name", t.content, t.abstract, c.name as "category"
            FROM text t JOIN category c ON t.category_id = c.id
            WHERE lower(t.name) LIKE "%"""+string.lower()+"""%" 
            OR lower(t.content) LIKE "%"""+string.lower()+"""%" 
            ORDER BY t.position
            """
        self.cursor.execute(sql)
        return self.cursor.fetchall()
