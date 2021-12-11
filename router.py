from app import app
from libs.utils.router import router

from middlewares.authentication import authentication

from controllers.auth    import auth
from controllers.user    import user
from controllers.device  import device
from controllers.urent   import urent
from controllers.ureturn import ureturn


# Auth route
router.post(url='/auth/login',  controller=auth.login)
router.post(url='/auth/signup', controller=auth.signup)

# User route
router.get(url='/user', authentication=authentication, controller=user.info)

# Device route
router.get(url='/devices',            controller=device.infos)
router.get(url='/device/<device_id>', controller=device.info)

# Rent route
router.get(url='/device/<device_id>/rent', controller=urent.checkAvailable)

# Return route
router.get(url='/device/<device_id>/return', controller=ureturn.checkAvailable)