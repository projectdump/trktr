from bottle import route, template, request, response, redirect
from app.util.validate import logged_in

@route("/admin/stuff")
def impressum():
    if logged_in(request):
        f = open('app/route/impressum.txt', 'r')
        g = open('app/route/footer.txt', 'r')
        h = open('app/route/meta.txt', 'r')
        d= h.readline()
        k= h.readline()
        a= h.readline()
        impressum = f.read()
        footer = g.read()

        data = f.read()
        return template('admin/stuff.tpl',
            impressum = impressum,
            description = d,
            keywords = k,
            author = a,
            footer = footer
        )

@route("/admin/stuff", method="post")
def impressum():
    if logged_in(request):
        impressum = request.POST.get('impressum', '').strip()
        footer = request.POST.get('footer', '').strip()
        description = request.POST.get('description', '').strip()
        keywords = request.POST.get('keywords', '').strip()
        author= request.POST.get('author', '').strip()
        f = open('app/route/impressum.txt', 'w')
        f.write(impressum)
        f.close()
        f = open('app/route/footer.txt', 'w')
        f.write(footer)
        f.close()
        f = open('app/route/meta.txt', 'w')
        f.write(description + "\n" + keywords + "\n" + author)
        f.close()
        redirect('/admin/stuff')
