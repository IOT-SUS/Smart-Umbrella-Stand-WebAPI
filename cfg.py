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
    TOKEN_FAKE        = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50IjoiMTEwNjEwODExNyIsIl9pZCI6IjYwY2FkMGQ3YzE1MzhlMTg2NjQ3OTIwZCIsInN0dWRlbnRfaWQiOiIxMTA2MTA4MTE3IiwiY3JlYXRlZF9hdCI6IjIwMjEtMDYtMTdUMDQ6MzQ6MzEuMDczWiIsInVwZGF0ZWRfYXQiOiIyMDIxLTA2LTE3VDA0OjM0OjMxLjA3M1oiLCJfX3YiOjAsInJlbWFyayI6ImFkbWluIiwiaWF0IjoxNjI2OTYzNzQ5LCJleHAiOjE2MjcwNTAxNDl9.tjoOVQWCJbRvB3CjknQ6_cHU0lr8bGaQF9D9Aok-Zl0"
    TOKEN_SECRET_KEY  = "]9!YF%'-rp6>GYJ(Hc&r"
    TOKEN_EXPIRE_TIME = 30  