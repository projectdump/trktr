from app.dao.picture import Picture
from app.dao.category import Category
from app.util.validate import logged_in
from app.util.request import saved
from bottle import route, template, request, response, redirect
import json
import urllib

@route('/admin/picture')
@route('/admin/picture/')
def admin_picture():
    if logged_in(request):
        return template('admin/picture/all', pictures = Picture().all(),
            categories = Category().picture_categories(), sortable = False)

@route('/admin/picture/new')
@route('/admin/picture/new/')
def admin_picture_new_form():
    if logged_in(request):
        return template('admin/picture/new', categories = Category().picture_categories())

@route('/admin/picture/new', method = "POST")
@route('/admin/picture/new/', method = "POST")
def admin_picture_new():
    if logged_in(request):
        Picture().insert(request.POST)
        redirect('/admin/picture')

@route('/admin/picture/:id/edit')
@route('/admin/picture/:id/edit/')
def admin_picture_edit(id):
    if logged_in(request):
        return template('admin/picture/edit', picture = Picture().by_id(id),
            categories = Category().picture_categories())

@route('/admin/picture/edit', method = "POST")
@route('/admin/picture/edit/', method = "POST")
def admin_picture_edit():
    if logged_in(request):
        Picture().update(request.POST)
        redirect('/admin/picture')

@route('/admin/picture/category/:id')
@route('/admin/picture/category/:id/')
def admin_picture_category(id):
    if logged_in(request):
        return template('admin/picture/all', pictures = Picture().by_category(id),
            categories = Category().picture_categories(), sortable=True)

@route('/admin/picture/sort/:json_string')
def admin_video_sort(json_string):
    id_list = json.loads(urllib.unquote(json_string))
    i = 1
    for id in id_list:
        print id, i
        Picture().update_position(id, i)
        i = i+1

@route('/admin/picture/:id/delete')
@route('/admin/picture/:id/delete/')
def admin_picture_delete(id):
    if logged_in(request):
        Picture().delete(id)
        redirect('/admin/picture')
