from bottle import route, template, request, response, redirect

@route("/admin/startpage")
def start_page():
    f = open('app/route/startpagestring.txt', 'r')
    startpage = f.read()
    return template('admin/startpage', url = startpage)

@route("/admin/startpage", method="POST")
def save_start_page():
    startpage = request.POST.get('url', '').strip()
    f = open('app/route/startpagestring.txt', 'w')
    f.write(startpage)
    f.close()
    redirect('/admin/startpage')
