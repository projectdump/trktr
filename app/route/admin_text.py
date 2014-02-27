from app.dao.text import Text
from app.dao.category import Category
from app.util.validate import logged_in
from app.util.request import saved
from bottle import route, template, request, response, redirect
import json
import urllib

@route('/admin/text')
@route('/admin/text/')
def admin_text():
    if logged_in(request):
        return template('admin/text/all.tpl', 
            texts = Text().get_metas(),
            categories = Category().text_categories(),
            sortable = False)

@route('/admin/text/category/:id')
@route('/admin/text/category/:id/')
def admin_text_category(id):
    if logged_in(request):
        return template('admin/text/all', texts = Text().by_category(id),
            categories = Category().text_categories(), sortable=True)

@route('/admin/text/new')
@route('/admin/text/new/')
def admin_text_new_form():
    if logged_in(request):
        return template('admin/text/new', categories = Category().text_categories())

@route('/admin/text/new', method = "POST")
@route('/admin/text/new/', method = "POST")
def admin_text_new():
    if logged_in(request):
        request.POST['home'] = request.forms.get('home')
        request.POST['footer'] = request.forms.get('footer')
        request.POST['sidebar'] = request.forms.get('sidebar')
        Text().insert(request.POST)
        redirect('/admin/text')

@route('/admin/text/:id/edit')
@route('/admin/text/:id/edit/')
def admin_text_edit(id):
    if logged_in(request):
        text = Text().by_id(id)
        stringdict = {}
        # set sizestring depending on `size` (int) in db
        if text['size'] == 1:
            stringdict['sizestring'] = 'small'
        elif text['size'] == 2:
            stringdict['sizestring'] = 'mid'
        elif text['size'] == 3:
            stringdict['sizestring'] = 'big'
        
        # set formatstring depending on `format` (int) in db 
        if text['format'] == 0:
            stringdict['formatstring'] = "landscape"
        elif text['format'] == 1:
            stringdict['formatstring'] = "portrait"
        
        # set alignmentstring depending on `alignment` (int) in db
        if text['alignment'] == -1:
            stringdict['alignmentstring'] = "left"
        elif text['alignment'] == 0:
            stringdict['alignmentstring'] = "center"
        elif text['alignment'] == 1:
            stringdict['alignmentstring'] = "right"
        
        # set overlapstring depending on `overlap` (int) in db
        if text['overlap'] == 1:
            stringdict['overlapstring'] = "light"
        elif text['overlap'] == 2:
            stringdict['overlapstring'] = "medium"
        elif text['overlap'] == 3:
            stringdict['overlapstring'] = "strong"
        return template('admin/text/edit', text = text, textinfo = stringdict, categories = Category().text_categories())

@route('/admin/text/edit', method = "POST")
@route('/admin/text/edit/', method = "POST")
def admin_text_edit():
    if logged_in(request):
        request.POST['home'] = request.forms.get('home')
        request.POST['footer'] = request.forms.get('footer')
        request.POST['sidebar'] = request.forms.get('sidebar')
        Text().update(request.POST)
        redirect('/admin/text')

@route('/admin/text/:id/delete')
@route('/admin/text/:id/delete/')
def admin_text_delete(id):
    if logged_in(request):
        Text().delete(id)
        redirect('/admin/text')

@route('/admin/text/sort/:json_string')
def admin_text_sort(json_string):
    id_list = json.loads(urllib.unquote(json_string))
    for id, i in zip(id_list, range(1, len(id_list)+1)):
        Text().update_position(id, i)
