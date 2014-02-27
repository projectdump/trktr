from ..util import get_connection

class Link:
    def __init__(self):
        self.conn = get_connection.setup()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def all(self):
        sql = "SELECT id, name, href, position FROM link ORDER BY position"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_names():
        sql = "SELECT name FROM link ORDER BY position"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def by_id(self, id):
        sql = "SELECT id, name, href, position FROM link WHERE id = ?"
        self.cursor.execute(sql, [id])
        return self.cursor.fetchone()

    def by_position(self, position):
        sql = "SELECT id, name, href, position FROM link WHERE position = ?"
        self.cursor.execute(sql, [int(position)])
        return self.cursor.fetchone()

    def get_metas(self):
        sql = "SELECT id, name, href, position FROM link ORDER BY position"
        self.cursor.execute(sql)
        return  self.cursor.fetchall()

    def insert(self, data):
        sql = 'SELECT MAX(position) AS "position" FROM link'
        self.cursor.execute(sql)
        position = self.cursor.fetchone()['position']
        if position == None:
            position = 0;
        position = position + 1
        sql = """
            INSERT INTO link(`name`, `href`, `position`) VALUES( ?, ?, ?)
            """
        self.cursor.execute(sql, (data['name'], data['href'], str(position)))

    def update(self, data):
        sql = """
            UPDATE link SET name = ?, href = ?
            WHERE id = ?
            """
        self.cursor.execute(sql, (data['name'], data['href'], data['id']))

    def update_position(self, id, position):
        sql = "UPDATE link SET position = ? WHERE id = ?"
        self.cursor.execute(sql, (position, id))

    def delete(self, id):
        sql = "DELETE FROM link WHERE id = ?"
        self.cursor.execute(sql, [id])
