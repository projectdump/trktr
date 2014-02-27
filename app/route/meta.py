from bottle import route, template, request, response, redirect
from app.util.validate import logged_in

@route("/admin/meta")
def meta_show():
    if logged_in(request):
        f = open('app/route/meta.txt', 'r')
        d= f.readline()
        k= f.readline()
        a= f.readline()
        f.close()
        return template('admin/keywords/edit', description = d, keywords = k, author = a)

@route("/admin/meta", method="POST")
def meta_update():
    if logged_in(request):
        description = request.POST.get('description', '').strip()
        keywords = request.POST.get('keywords', '').strip()
        author= request.POST.get('author', '').strip()
        f = open('app/route/meta.txt', 'w')
        f.write(description + "\n" + keywords + "\n" + author)
        f.close()
        redirect('/admin/meta')
