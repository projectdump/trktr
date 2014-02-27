from bottle import route, template, request, response, redirect
from app.dao.helper import Helper
from app.dao.category import Category 

@route("/")
def landing():
    categories = Category().text_categories()
    c = categories[0]
    return template(c['template'], helper = Helper(c['name']))

@route("/:category")
def landing_category(category):
    print category
    c = Category().by_name(category)
    return template(c['template'], helper = Helper(category))
