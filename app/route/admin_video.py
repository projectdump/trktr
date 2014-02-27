import json
import urllib
import app.util.playlist as playlist

from app.dao.video import Video
from app.dao.category import Category
from app.util.validate import logged_in
from app.util.request import saved
from bottle import route, template, request, response, redirect

@route('/admin/video')
@route('/admin/video/')
def admin_video():
    if logged_in(request):
        return template('admin/video/all', videos = Video().all(),
            categories = Category().video_categories(), sortable=False)

@route('/admin/video/category/:id')
@route('/admin/video/category/:id/')
def admin_video_category(id):
    if logged_in(request):
        return template('admin/video/all', videos = Video().by_category(id),
            categories = Category().video_categories(), sortable=True)

@route('/admin/video/new')
@route('/admin/video/new/')
def admin_video_new_form():
    if logged_in(request):
        return template('admin/video/new', categories = Category().video_categories())

@route('/admin/video/new', method = "POST")
@route('/admin/video/new/', method = "POST")
def admin_video_new():
    if logged_in(request):
        Video().insert(request.POST)
        redirect('/admin/video')

@route('/admin/video/:id/edit')
@route('/admin/video/:id/edit/')
def admin_video_edit_form(id):
    if logged_in(request):
        return template('admin/video/edit', categories = Category().video_categories(),
            video = Video().by_id(id))

@route('/admin/video/:id/edit', method = "POST")
@route('/admin/video/:id/edit/', method = "POST")
def admin_video_edit(id):
    if logged_in(request):
        Video().update(request.POST)
        redirect('/admin/video')

@route('/admin/video/:id/delete')
@route('/admin/video/:id/delete/')
def admin_video_delete(id):
    if logged_in(request):
        Video().delete(id)
        redirect('/admin/video')

@route('/admin/video/sort/:json_string')
def admin_video_sort(json_string):
    id_list = json.loads(urllib.unquote(json_string))
    i = 1
    for id in id_list:
        print id, i
        Video().update_position(id, i)
        i = i+1
