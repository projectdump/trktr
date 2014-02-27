from app.dao.category import Category
from app.util.validate import logged_in
from app.util.request import saved
from bottle import route, template, request, response, redirect
import json
import urllib

@route('/admin/category')
@route('/admin/category/')
def admin_category():
    if logged_in(request):
        return template('admin/category/all', categories = Category().text_categories(), sortable=True )

@route('/admin/category/new')
@route('/admin/category/new/')
def admin_category_new():
    if logged_in(request):
        if saved(request):
            Category().create(request.GET)
            redirect('/admin/category')
        else:
            return template('admin/category/new', types = Category().types(), parents=Category().all())

@route('/admin/category/:id/edit')
@route('/admin/category/:id/edit/')
def admin_category_edit(id):
    if logged_in(request):
        if saved(request):
            Category().update(request.GET)
            redirect('/admin/category')
        else:
            return template('admin/category/edit', types = Category().types(), category = Category().by_id(id), parents = Category().all())

@route('/admin/category/:id/delete')
@route('/admin/category/:id/delete/')
def admin_category_delete(id):
    if logged_in(request):
        Category().delete(id)
        redirect('/admin/category')

@route('/admin/category/sort/:json_string')
def admin_category_sort(json_string):
    id_list = json.loads(urllib.unquote(json_string))
    i = 1
    for id in id_list:
        Category().update_position(id, i)
        i = i+1
