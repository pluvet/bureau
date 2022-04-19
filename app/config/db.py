import os
from urllib.parse import quote_plus
from pymongo import MongoClient

#user = os.environ['MONGO_DB_USERNAME']
#password = os.environ['MONGO_DB_PWD']
socket = "localhost:27017/test"
user = "none"


if user != "none":
    conn = MongoClient('mongodb://admin:123456@mongodb/test?authSource=admin&authMechanism=SCRAM-SHA-256')
else:
    conn = MongoClient('mongodb://admin:123456@mongodb/test?authSource=admin&authMechanism=SCRAM-SHA-256')

#uri = "mongodb://%s:%s@%s" % (
#    quote_plus(user), quote_plus(password), quote_plus(socket)
#)

#conn = MongoClient(uri)
