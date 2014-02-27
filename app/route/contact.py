from bottle import route, template, request, response, redirect

@route("/admin/contact")
def contact():
    f = open('app/route/contact.txt', 'r')
    data = f.read()
    return template('admin/contact', contact = data)

@route("/admin/contact", method="post")
def save_contact():
    contact = request.POST.get('contact', '').strip()
    f = open('app/route/contact.txt', 'w')
    f.write(contact)
    f.close()
    redirect('/admin/contact')
