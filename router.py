from app import app

from libs.utils.router import router

from controllers.auth     import auth
from controllers.user     import user
from controllers.urrs     import urrs
from controllers.urent    import urent
from controllers.device   import device
from controllers.ureturn  import ureturn
from controllers.umbrella import umbrella

from middlewares.authentication      import authentication
from middlewares.adminAuthentication import adminAuthentication

# ============================================================================
# "                         FRONTEND HTML PAGE                               "
# ============================================================================

# Web page
router.render_page(url='/'      , template='index.html')
router.render_page(url='/rent'  , template='rent.html')
router.render_page(url='/member', template='member.html')
router.render_page(url='/signup', template='signupform.html')
router.render_page(url='/login' , template='loginform.html')
router.render_page(url='/fund'  , template='fund.html')


# ============================================================================
# "                             BACKEND API                                  "
# ============================================================================

# Auth api
router.post(url='/api/auth/login' , controller=auth.login)
router.post(url='/api/auth/signup', controller=auth.signup)

# User api
router.get (url='/api/user'       , authentication=authentication, controller=user.info)
router.post(url='/api/user/update', authentication=authentication, controller=user.update)
router.post(url='/api/user/delete', authentication=authentication, controller=user.delete)

# Device route
router.get (url='/api/devices'                         , controller=device.infos)
router.get (url='/api/device/<device_id>'              , controller=device.info)
router.post(url='/api/device/add'                      , controller=device.add)
router.post(url='/api/device/update/<device_id>'       , controller=device.update)
router.post(url='/api/device/update_status/<device_id>', controller=device.update_status)
router.post(url='/api/device/delete/<device_id>'       , controller=device.delete)

# Rent api
router.get (url='/api/rent/records'            , authentication=authentication, controller=urent.record)
router.get (url='/api/rent/records_all'        , authentication=authentication, controller=urent.records)
router.get (url='/api/rent/vacancy/<device_id>', controller=urent.checkAvailable)
router.post(url='/api/rent/success/<device_id>', controller=urent.success)
router.post(url='/api/rent/<device_id>'        , authentication=authentication, controller=urent.add)

# Return api
router.get (url='/api/return/vacancy/<device_id>', controller=ureturn.checkVacancy)
router.post(url='/api/return/success/<device_id>', controller=ureturn.success)
router.post(url='/api/return/<device_id>'        , controller=ureturn.add)

# RRs api
router.get (url='/api/rrs/<rrs_id>'                                  , controller=urrs.info)
router.get (url='/api/rrs/polling/action/<action>/device/<device_id>', controller=urrs.devicePolling)
router.get (url='/api/rrs/polling/action/<action>/user'              , authentication=authentication, controller=urrs.userPolling)

# Umbrella api
router.get (url='/api/umbrella/record/<user_id>', authentication=authentication, controller=umbrella.record)
router.get (url='/api/umbrella/records'         , authentication=authentication, controller=umbrella.records)
router.post(url='/api/umbrella/add'             , controller=umbrella.add)