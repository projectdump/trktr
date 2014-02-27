from app.dao.link import Link
from app.util.validate import logged_in
from app.util.request import saved
from bottle import route, template, request, response, redirect
import json
import urllib

@route('/admin/link')
@route('/admin/link/')
def admin_link():
    if logged_in(request):
        return template('admin/link/all', links = Link().get_metas(), sortable = False)
        

@route('/admin/link/new')
@route('/admin/link/new/')
def admin_link_new_form():
    if logged_in(request):
        return template('admin/link/new')

@route('/admin/link/new', method = "POST")
@route('/admin/link/new/', method = "POST")
def admin_link_new():
    if logged_in(request):
        Link().insert(request.POST)
        redirect('/admin/link')

@route('/admin/link/:id/edit')
@route('/admin/link/:id/edit/')
def admin_link_edit(id):
    if logged_in(request):
        return template('admin/link/edit', link = Link().by_id(id))

@route('/admin/link/edit', method = "POST")
@route('/admin/link/edit/', method = "POST")
def admin_link_edit():
    if logged_in(request):
        Link().update(request.POST)
        redirect('/admin/link')

@route('/admin/link/:id/delete')
@route('/admin/link/:id/delete/')
def admin_link_delete(id):
    if logged_in(request):
        Link().delete(id)
        redirect('/admin/link')

@route('/admin/link/sort/:json_string')
def admin_link_sort(json_string):
    id_list = json.loads(urllib.unquote(json_string))
    for id, i in zip(id_list, range(1, len(id_list)+1)):
        Link().update_position(id, i)
