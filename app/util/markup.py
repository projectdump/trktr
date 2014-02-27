from ..dao.text import Text
from ..dao.picture import Picture
from ..dao.category import Category
from ..dao.link import Link
import os


class Markup():
    def top_menu():
         = Category().by_top_menu()
   

class Markup():
    def __init__(self, params, render_page = False, render_gallery = False, render_text = False,
        cv = False, contact = False, links = False, req = None):
        self.gallery = params['gallery']
        self.picture = params['picture']
        self.text= params['text']
        self.render_page = render_page
        self.render_gallery = render_gallery
        self.render_text = render_text
        self.cv = cv
        self.contact = contact
        self.links = links
        self.req = req
        f = open('app/route/meta.txt')
        self.description = f.readline().strip('\n')
        self.keywords = f.readline().strip('\n')
        self.author = f.readline().strip('\n')
        f.close()

    def keywords(self):
        return self.keywords

    def description(self):
        return self.description

    def author(self):
        return self.author

    def pages(self):
        out = ""
        if(self.render_gallery):
            out += "<a href = \"/gallery\" class=\"slide active\">work</a>"
        else:
            out += "<a href = \"/gallery\" class=\"slide\">work</a>"
        out += " / "
        if(self.render_text):
            out += "<a href = \"/text\" class=\"slide active\">text</a>"
        else:
            out += "<a href = \"/text\" class=\"slide\">text</a>"
        out += " / "
        if(self.cv):
            out += "<a href = \"/cv\" class=\"active\">cv</a>"
        else:
            out += "<a href = \"/cv\" >cv</a>"
        out += " / "
        if(self.contact):
            out += "<a href = \"/contact\" class=\"active\">contact</a>"
        else:
            out += "<a href = \"/contact\" >contact</a>"
        out += " / "
        if(self.links):
            out += "<a href = \"/links\" class=\"active\">links</a>"
        else:
            out += "<a href = \"/links\" >links</a>"
        return out

    def gallery_control(self):
        out = ""
        if(self.render_gallery and self.picture != None):
            prev_pic = 1
            next_pic = 1
            picture_max_position = len(Picture().by_category_position(self.gallery['position']))
            if(self.picture['position'] > 1):
                prev_pic = self.picture['position']-1
                out += "<a href=\"/gallery/"+str(self.gallery['position'])+"/"+str(prev_pic)+"\" class = \"prev\">&lt;</a>"
            out += " " + str(self.picture['position']) + " / " + str(picture_max_position) + " "
            if(self.picture['position'] < picture_max_position):
                next_pic = self.picture['position']+1
                out += "<a href=\"/gallery/"+str(self.gallery['position'])+"/"+str(next_pic)+"\" class = \"next\">&gt;</a>"
        else:
            out += '<span style="visibility:hidden"><< >></span>'
        return out

    def menu(self):
        out = ""
        out += "<ul>"
        if(self.render_gallery):
            galleries = Category().all()
            for gallery in galleries:
                if(self.render_gallery == True):
                    if(self.gallery['id'] == gallery['id']):
                        out += "<li><a href=\"/gallery/"+str(gallery['position'])+"\" "
                        out += "class=\"active\">"+str(gallery['name'])+"</a></li>"
                    else:
                        out += "<li><a href=\"/gallery/"+str(gallery['position'])+"\">"
                        out += gallery['name']+"</a></li>"
                #else:
                #    out += "<li><a href=\"/gallery/"+str(gallery['position'])+"\">"
                #    out += gallery['name']+"</a></li>"
        if(self.render_text):
            texts = Text().all()
            for text in texts:
                if(self.render_text == True):
                    if(self.text['id'] == text['id']):
                        out += "<li><a href=\"/text/"+str(text['position'])+"\" "
                        out += "class=\"active\">"+str(text['name'])+"</a></li>"
                    else:
                        out += "<li><a href=\"/text/"+str(text['position'])+"\">"
                        out += text['name']+"</a></li>"
                #else:
                #    out += "<li><a href=\"/gallery/"+str(gallery['position'])+"\">"
                #    out += gallery['name']+"</a></li>"
        out += "</ul>"
        return out

    def menudisplay(self):
        f =  open('app/util/slidedowntoggle.txt', 'r')
        toggle = f.readline().strip("\n")
        last = f.readline().strip("\n")
        f.close()
        fw = open('app/util/slidedowntoggle.txt', 'w')
        if((self.render_gallery) and toggle == '0'):
            fw.write('0\ngallery')
            fw.close()
            if(last == 'gallery'):
                return "block"
            else:
                return "none"
        if((self.render_gallery) and toggle == '1'):
            fw.write('0\ngallery')
            fw.close()
            return "none"
        if((self.render_text) and toggle == '0'):
            fw.write('0\ntext')
            fw.close()
            if(last == 'text'):
                return "block"
            else:
                return "none"
        if((self.render_text) and toggle == '1'):
            fw.write('0\ntext')
            fw.close()
            return "none"
        else:
            fw.write('1')
            fw.close()
            return "none"

    def content(self):
        out = ""
        if(self.render_gallery and self.picture != None):
            prev_pic = 1
            next_pic = 1
            picture_max_position = len(Picture().by_category_position(self.gallery['position']))
            a = ""
            if(self.picture['position'] == picture_max_position):
                a = "<a href=\"/gallery/"+str(self.gallery['position'])+"/1\" class = \"prev\">"
            if(self.picture['position'] < picture_max_position):
                next_pic = self.picture['position']+1
                a = "<a href=\"/gallery/"+str(self.gallery['position'])+"/"+str(next_pic)+"\" class = \"next\">"
            out += "<div class=\"gallery\">\n   "
            out += a
            out += "<img class = \"gallery\" src = \"/"+self.resized_picture_path()+"\" alt=\""+self.picture['title']+", "+self.picture['description']+"\">"
            out += "</a>"
            out += "</div>"
            out += """
            <div class = \"picture-info\">
                <ul>
                    <li>
                        <i>"""+self.picture['title']+"""</i> 
                    </li>
                    <li>
                        """+self.picture['description']+"""
                    </li>
                </ul>
            </div>"""
        if(self.render_text):
            out += self.text['content']
        if(self.render_page):
            if(self.cv):
                f = open('app/route/cv.txt', 'r')
                out += f.read()
                f.close()
            if(self.contact):
                f = open('app/route/contact.txt', 'r')
                out += f.read()
                f.close()
            if(self.links):
                links = Link().all()
                out += "<ul class = \"links\">"
                for link in links:
                    out += "<li><a href = \""+link['href']+"\" target = \"_blank\">"+link['name']+"</a></li>"
                out += "</ul>"
        return out

    def resized_picture_path(self):
        fn, ext = os.path.splitext(self.picture['path'])
        return 'assets/picture'+str(self.picture['id'])+'res'+ext

    def startpage(self):
        f = open('app/route/startpagestring.txt', 'r')
        url = f.read()
        f.close()
        return url
