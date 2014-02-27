from ..util import get_connection
from app.dao.category import Category
from app.dao.text import Text
from app.dao.picture import Picture
import urllib
import random

class Helper:
    def __init__(self, category):
        self.conn = get_connection.setup()
        self.cursor = self.conn.cursor()
        self.category = category

    #def __del__(self):
    #    self.cursor.close()
    #    self.conn.commit()
    #    self.conn.close()
    
    def header_image(self):
        sql = """SELECT * FROM picture JOIN category ON
            picture.category_id = category.id
            WHERE name = "header"
            """
        self.cursor.execute(sql)
        pics = self.cursor.fetchall()
        pic = pics[random.randint(0, len(pics)-1)]
        return "<img src = \""+pic['path']+"\">"

    def entries(self):
        sql = """
            SELECT * FROM text
                JOIN category ON text.category_id = category.id
            WHERE category.name = ?
            ORDER BY text.position
            """
        self.cursor.execute(sql, (self.category,))
        texts = self.cursor.fetchall()
        html = ""
        for text in texts:
            html += self.entry(text)
        return html

    def entry(self, text):
        # set CSS class for boxes
        cssclass = "entry"
        # size
        if text['size'] == 1:
            cssclass += " fourtwofive"
        elif text['size'] == 2:
            cssclass += " sixfourtwo"
        elif text['size'] == 3:
            cssclass += " seveneightone"
        if text['format'] == 0:
            cssclass += "-l"
        elif text['format'] == 1:
            cssclass += "-p"
        # alignment
        if text['alignment'] == -1:
            cssclass += " pull-left"
        elif text['alignment'] == 0:
            cssclass += " center"
        elif text['alignment'] == 1:
            cssclass += " pull-right"
        # overlap
        if text['overlap'] == 1:
            if text['alignment'] == -1:
                cssclass += " overlap1l"
            elif text['alignment'] == 0:
                cssclass += " overlap1c"
            elif text['alignment'] == 1:
                cssclass += " overlap1r"
        elif text['overlap'] == 2:
            if text['alignment'] == -1:
                cssclass += " overlap2l"
            elif text['alignment'] == 0:
                cssclass += " overlap2c"
            elif text['alignment'] == 1:
                cssclass += " overlap2r"
        elif text['overlap'] == 3:
            if text['alignment'] == -1:
                cssclass += " overlap3l"
            elif text['alignment'] == 0:
                cssclass += " overlap3c"
            elif text['alignment'] == 1:
                cssclass += " overlap3r"

        print text['name']

        html = "<div class = \""+cssclass+"\">\n"
        html += "   <div class = \""+cssclass+" under\"></div>\n"
        html += "   <img src = \""+text['coverpic']+"\" class = \"img-responsive cover\">\n"
        html += "   <a class = \"box\">\n"
        html += "       <div class = \"blacklayer\">\n"
        html += text['abstract']
        html += "       </div>\n"
        html += "   </a>\n"
        html += "   <div class = \"boxcontent\">\n"
        html += "       <div class = \"x\"></div>\n"
        html += "       <div class = \"content\">\n"
        html += text['content']
        html += "       </div>\n"
        html += "   </div>\n"
        html += "</div>\n"
        return html

    def list(self):
        sql = """
            SELECT * FROM text
                JOIN category ON text.category_id = category.id
            WHERE category.name = ?
            ORDER BY text.position
            """
        self.cursor.execute(sql, (self.category,))
        texts = self.cursor.fetchall()
        html = ""
        i = 1
        for text in texts:
            print i 
            html += "<div class = \"bg"+str(i%2)+"\">\n"
            html += "   <div class = \"marketing\">\n"
            html += text['content']
            html += "   </div>\n"
            html += "   <div class = \"up\"></div>\n"
            html += "</div>\n"
            i = i + 1
        print html
        return html

    def menu(self):
        sql = """SELECT category.name as "name"
                 FROM category JOIN category_type
                    ON category.category_type_id = category_type.id
                 WHERE category_type.name = "text"
                 ORDER BY category.position
              """
        self.cursor.execute(sql)
        categories = self.cursor.fetchall()
        html = ""
        for c in categories:
            url = c['name'].replace(" ", "-")
            html += "<li><a href = \""+url+"\">"+c['name']+"</a></li>"
        return html

    def footer(self):
        f = open("app/route/footer.txt")
        footer = f.read()
        f.close()
        return footer
