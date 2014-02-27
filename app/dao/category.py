from ..util import get_connection

class Category:
    def __init__(self):
        self.conn = get_connection.setup()
        self.cursor = self.conn.cursor()

    def all(self):
        sql = """
            SELECT c.name as "name", t.name as "type", c.id as "id",
                c.position as "position", c.template as "template",
                c.parent as "parent", p.name as "parent_name"
            FROM category c 
                JOIN category_type t
                    ON c.category_type_id = t.id
                LEFT JOIN category p
                    ON c.parent = p.id
            ORDER BY position
            """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def by_id(self, id):
        sql = """
            SELECT c.name as "name", t.name as "type", c.category_type_id, c.id as "id",
                c.position as "position", c.template as "template",
                c.parent as "parent", p.name as "parent_name"
            FROM category c JOIN category_type t
            ON c.category_type_id = t.id
                LEFT JOIN category p
                    ON c.parent = p.id
            WHERE c.id = ?
            """
        print sql, id
        self.cursor.execute(sql, [id])
        return self.cursor.fetchone()

    def by_name(self, name):
        sql = """
            SELECT c.name as "name", t.name as "type", c.category_type_id, c.id as "id",
                c.position as "position", c.template as "template",
                c.parent as "parent", p.name as "parent_name"
            FROM category c JOIN category_type t
            ON c.category_type_id = t.id
                LEFT JOIN category p
                    ON c.parent = p.id
            WHERE c.name = ?
            """
        self.cursor.execute(sql, (name,))
        return self.cursor.fetchone()

    def by_position(self, position):
        sql = """
            SELECT c.name as "name", t.name as "type", c.category_type_id, c.id as "id",
                   c.position as "position"
            FROM category c JOIN category_type t
            ON c.category_type_id = t.id
            WHERE c.position = ?
            """
        self.cursor.execute(sql, position)
        return self.cursor.fetchone()

    def types(self):
        sql = """
            SELECT name, id FROM category_type
            """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def video_categories(self):
        sql = """
            SELECT c.name as "name", c.id as "id" FROM category c
            JOIN category_type t ON t.id = c.category_type_id
            WHERE t.id = 4 OR t.name = "video"
            """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def picture_categories(self):
        sql = """
            SELECT c.name as "name", c.id as "id" FROM category c
            JOIN category_type t ON t.id = c.category_type_id
            WHERE t.id = 2 OR t.name = "picture"
            ORDER BY c.position
            """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def text_categories(self):
        sql= """
            SELECT c.name as "name", t.name as "type", c.id as "id",
                c.position as "position", c.template as "template",
                c.parent as "parent", p.name as "parent_name"
            FROM category c 
                JOIN category_type t
                    ON c.category_type_id = t.id
                LEFT JOIN category p
                    ON c.parent = p.id
            WHERE t.name = "text"
            ORDER BY position
            """
        #sql = """
        #    SELECT c.name as "name", c.id as "id", p.name as "parent"
        #    FROM category c
        #    JOIN category_type t ON t.id = c.category_type_id
        #    LEFT JOIN category p ON p.id = c.parent
        #    WHERE t.id = 3 OR t.name = "text"
        #    ORDER BY c.position
        #    """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def create(self, data):
        assert data['name'] != ""
        assert data['category_type_id'] != ""
        template = None
        try:
            template = data['template']
        except KeyError:
            template = ""
        if template == None:
            print "\n\ntrololol\n\n"
        else:
            print "\n\ntrololololololol\n" + str(template)
        parent = None if data['parent'] == "NULL" else int(data['parent'])
        sql = 'SELECT MAX(position) AS "position" FROM category'
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        position = row['position']
        if position == None:
            position = 0;
        position = position + 1
        sql = """
            INSERT INTO category (name, category_type_id, position, template, parent)
            VALUES(?, ?, ?, ?, ?);
            """
        self.cursor.execute(sql, (data['name'], data['category_type_id'], position, template, parent))

    def update(self, data):
        assert data['id'] != ""
        assert data['name'] != ""
        assert data['category_type_id'] != ""
        template = None
        try:
            template = data['template']
            print template
        except KeyError:
            template = ""
        parent = None if data['parent'] == "" else int(data['parent'])
        sql = """
            UPDATE category SET name = ?, category_type_id = ?, template = ?,
                parent = ?
            WHERE id = ?
            """
        self.cursor.execute(sql, (data['name'], data['category_type_id'], template, data['parent'], data['id']))

    def update_position(self, id, position):
        sql = "UPDATE category SET position = ? WHERE id = ?"
        self.cursor.execute(sql, (position, id))

    def delete(self, id):
        assert id != ""
        sql = "DELETE FROM category WHERE id = ?"
        self.cursor.execute(sql, (id,))

    def __del__(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
