from ..util import get_connection
from ..util.transformer import make_webm
import os
import urlparse

class Video:
    def __init__(self):
        self.conn = get_connection.setup()
        print self.conn
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def all(self):
        sql = """
            SELECT v.id, v.title, v.description, v.path, v.thumbnail,
                v.position, c.name as "category", v.category_id
            FROM video v JOIN category c
            ON v.category_id = c.id
            ORDER BY category, v.position
            """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def all_for_jwplayer(self):
        sql = """
            SELECT video.path as "file", video.title, video.description, video.thumbnail
            FROM video JOIN category
            ON video.category_id = category.id
            ORDER BY video.category_id, video.position
            """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def by_category(self, category_id):
        sql = """
            SELECT v.id, v.title, v.description, v.path, v.thumbnail,
                v.position, c.name as "category", v.category_id
            FROM video v JOIN category c
            ON v.category_id = c.id
            WHERE v.category_id = ?
            ORDER BY v.position
            """
        self.cursor.execute(sql, [category_id])
        return self.cursor.fetchall()

    def by_id(self, id):
        sql = """
            SELECT v.id, v.title, v.description, v.path, v.thumbnail,
                v.position, c.name as "category", v.category_id
            FROM video v JOIN category c
            ON v.category_id = c.id
            WHERE v.id = ?
            """
        self.cursor.execute(sql, [id])
        return self.cursor.fetchone()

    def insert(self, data):
        assert data['title'] != ""
        assert data['video'] != "" or data['youtube'] != ""
        sql = 'SELECT MAX(position) AS "position" FROM video WHERE category_id = ?'
        self.cursor.execute(sql, [data['category_id']])
        row = self.cursor.fetchone()
        position = row['position']
        if position == None:
            position = 0;
        position = position + 1
        sql = """
            INSERT INTO video(`title`, `description`, `position`, `category_id`)
            VALUES( ?, ?, ?, ?)
            """
        self.cursor.execute(sql, (data['title'], data['description'],
            str(position), data['category_id']))
        sql = "SELECT MAX(id) AS 'id' FROM video"
        self.cursor.execute(sql)
        id = str(self.cursor.fetchone()['id'])
        if "youtu" in data['youtube']:
            print data['youtube']
            sql = "UPDATE video SET path = ?, thumbnail = ? WHERE id = ?"
            videopath = data['youtube']
            videodata = urlparse.urlparse(videopath)
            query = urlparse.parse_qs(videodata.query)
            vid = query['v'][0]
            thumbnailpath = "http://img.youtube.com/vi/"+vid+"/hqdefault.jpg"
            self.cursor.execute(sql, (videopath, thumbnailpath, id))
            return
        if data['thumbnail'] != "" and data['video'] != "":
            fn, ext = os.path.splitext(data['video'].filename)
            videopath = 'assets/video'+id+ext
            open(videopath, 'wb').write(data['video'].file.read())
            make_webm(videopath)
            fn, ext = os.path.splitext(data['thumbnail'].filename)
            thumbnailpath = 'assets/thumbnail'+id+ext
            open(thumbnailpath, 'wb').write(data['thumbnail'].file.read())
            sql = "UPDATE video SET path = ?, thumbnail = ? WHERE id = ?"
            self.cursor.execute(sql, (videopath, thumbnailpath, id))

    def update(self, data):
        assert data['title'] != ""
        sql = """
            UPDATE video SET title = ?, description = ?, category_id = ?
            WHERE id = ?
            """
        self.cursor.execute(sql, (data['title'], data['description'],
            data['category_id'], data['id']))
        if data['video'] != "":
            fn, ext = os.path.splitext(data['video'].filename)
            videopath = 'assets/video'+data['id']+ext
            open(videopath, 'wb').write(data['video'].file.read())
            make_webm(videopath)
        if data['thumbnail'] != "":
            fn, ext = os.path.splitext(data['thumbnail'].filename)
            thumbnailpath = 'assets/thumbnail'+data['id']+ext
            open(thumbnailpath, 'wb').write(data['thumbnail'].file.read())
        if "youtu" in data['youtube']:
            sql = "UPDATE video SET path = ?, thumbnail = ? WHERE id = ?"
            videopath = data['youtube']
            videodata = urlparse.urlparse(videopath)
            query = urlparse.parse_qs(videodata.query)
            vid = query['v'][0]
            thumbnailpath = "http://img.youtube.com/vi/"+vid+"/hqdefault.jpg"
            self.cursor.execute(sql, (videopath, thumbnailpath, data['id']))
            return

    def update_position(self, id, position):
        sql = "UPDATE video SET position = ? WHERE id = ?"
        self.cursor.execute(sql, (position, id))

    def delete(self, id):
        video = self.by_id(id);
        if "asset" in video['path']:
            try:
                os.unlink(video['path'])
                os.unlink(video['path']+".webm")
            except OSError, e:
                pass
            try:
                os.unlink(video['thumbnail']);
            except OSError, e:
                pass
        sql = "DELETE FROM video WHERE id = ?"
        self.cursor.execute(sql, [id])
