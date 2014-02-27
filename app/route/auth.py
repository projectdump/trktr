from bottle import route, template, request, response, redirect
from ..config import config

@route('/login', method = 'GET')
@route('/login/', method = "GET")
def login():
    return template('login')

@route('/validate', method = "POST")
def validate():
    formpw = request.POST.get("password", "").strip()
    formuser = request.POST.get("username", "").strip()
    f = open("app/route/password.txt", "r")
    pw = f.read().strip()
    f.close()
    if formpw == pw and formuser == "trktr":
        response.set_cookie('auth', 'true', secret = config['secret']);
        redirect('/admin/text')
    else:
        return "Wrong Password"

@route("/logout")
def logout():
    response.set_cookie("auth", "false", secret = "hahaha")
    redirect("/")
