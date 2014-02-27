from ..config import config

def auth(req, res):
    f = open('app/route/password.txt')
    pw = f.read().strip('\n')
    f.close()
    if req.get('password', '').strip() == pw:
        res.set_cookie('auth', 'true', secret = config['secret']);
        return True
    else:
        return False

def logged_in(req):
    auth = req.get_cookie('auth', secret = config['secret'])
    if (auth == 'true'):
        return True
    else:
        return False
