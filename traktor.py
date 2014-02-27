from bottle import debug, run, FlupFCGIServer
from app.config import config
from app.route.landing import *
from app.route.static import *
from app.route.admin_picture import *
from app.route.admin_category import *
from app.route.admin_video import *
from app.route.admin_text import *
from app.route.admin_link import *
#from app.route.meta import *
from app.route.password import *
from app.route.stuff import *
from app.route.contact import *
from app.route.auth import *

@route('/admin/index')
@route('/admin/index/')
def admin_index():
    if logged_in(request):
        return template('admin/landing')

debug(True)
run(server = FlupFCGIServer, port=11005, host="127.0.0.1")
