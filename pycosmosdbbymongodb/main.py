import os
import bson

from pymongo import MongoClient
from pymodm.connection import connect
from pymodm.manager import Manager
from pymodm import MongoModel, fields


db_name = os.getenv("MONGO_DB")
host = os.getenv("MONGO_HOST")
port = 10255
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
args = "ssl=true&retrywrites=false&ssl_cert_reqs=CERT_NONE"

connection_uri = f"mongodb://{username}:{password}@{host}:{port}/{db_name}?{args}"

client = MongoClient(connection_uri)

connect(connection_uri, alias="user")

db = client[db_name]
user_collection = db['user']

# Save to the DB
# user_collection.insert_one({"email": "amer@foobar.com"})

class User(MongoModel):
    _id=fields.ObjectIdField(primary_key=True)
    text=fields.CharField()

    class Meta:
        connection_alias='user'
        collection_name='user'
        final=True

s = User(_id=bson.ObjectId(), text='sumit').save()

# Query the DB
for user in user_collection.find():
    print(user)