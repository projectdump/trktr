from bottle import route, static_file

@route('/css/<path>')
def css(path):
    return static_file(path, root = "./css")

@route('/js/<path:path:path>')
def js(path):
    return static_file(path, root = "./js")

@route('/fonts/<path>')
def fonts(path):
    return static_file(path, root = "./fonts")

@route('/img/<path>')
def img(path):
    return static_file(path, root = "./img")

@route('/player/<path>')
def player(path):
    return static_file(path, root = "./player")

@route('/assets/<path>')
def asset(path):
    return static_file(path, root = "./assets")

@route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root = "./img")

