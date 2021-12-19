from app import app

from libs.utils.router import router

from middlewares.authentication      import authentication
from middlewares.adminAuthentication import adminAuthentication

from controllers.auth     import auth
from controllers.user     import user
from controllers.device   import device
from controllers.urent    import urent
from controllers.ureturn  import ureturn
from controllers.umbrella import umbrella

# ============================================================================
# "                         FRONTEND HTML PAGE                               "
# ============================================================================

# Home page
router.render_page(url='/',       template='index.html')
router.render_page(url='/rent',   template='rent.html')
router.render_page(url='/member', template='member.html')
router.render_page(url='/signup', template='signupform.html')
router.render_page(url='/login',  template='loginform.html')


# ============================================================================
# "                             BACKEND API                                  "
# ============================================================================

# Auth api
router.post(url='/api/auth/login',  controller=auth.login)
router.post(url='/api/auth/signup', controller=auth.signup)

# User api
router.get(url='/api/user', authentication=authentication, controller=user.info)
router.post(url='/api/user/update', authentication=authentication, controller=user.update)
router.post(url='/api/user/delete', authentication=authentication, controller=user.delete)

# Device route
router.get(url='/api/devices',                      controller=device.infos)
router.get(url='/api/device/<device_id>',           controller=device.info)
router.post(url='/api/device/add',                  controller=device.add)
router.post(url='/api/device/update/<device_id>',   controller=device.update)
router.post(url='/api/device/delete/<device_id>',    controller=device.delete)

# Rent api
router.get(url='/api/device/<device_id>/rent', controller=urent.checkAvailable)

# Return api
router.get(url='/api/device/<device_id>/return',  controller=ureturn.checkAvailable)
router.post(url='/api/device/<device_id>/return', controller=ureturn.returnUmbre)

# Umbrella api
router.post(url='/api/umbrella/add', controller=umbrella.add)
