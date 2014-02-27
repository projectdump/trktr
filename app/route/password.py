from bottle import route, template, request, response, redirect
from app.util.validate import logged_in

@route("/admin/password")
def password_edit():
    if logged_in(request):
        return template('admin/password/edit')

@route("/admin/password", method="POST")
def password_update():
    if logged_in(request):
        password = request.POST.get('oldpassword', '').strip()
        newpass = request.POST.get('newpassword', '').strip()
        newpass2 = request.POST.get('newpassword2', '').strip()
        f = open('app/route/password.txt', 'r')
        currentpassword = f.read().strip()
        f.close()
        if password == currentpassword and newpass == newpass2:
            f = open('app/route/password.txt', 'w')
            f.write(newpass)
            f.close()
        redirect('/admin/password')
