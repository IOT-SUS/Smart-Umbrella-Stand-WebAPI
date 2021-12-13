# Configure
class config():
    # Server Name
    SERVER_NAME  = "127.0.0.1:5000"

    # Database Constant
    MONGO_USERNAME = "root"
    MONGO_PASSWORD = "root"
    MONGO_ROUTE    = "35.236.177.163:27017"
    MONGO_DATABASE = "testdb"

    # Database Setting
    MONGO_URI = "mongodb://"+MONGO_USERNAME+":"+MONGO_PASSWORD+"@"+MONGO_ROUTE+"/"+MONGO_DATABASE+"?authSource=admin"

    # Json Web Token
    TOKEN_SECRET_KEY  = "]9!YF%'-rp6>GYJ(Hc&r"
    TOKEN_EXPIRE_TIME = 30  