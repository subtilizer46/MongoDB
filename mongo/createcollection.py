import pymongo

uri = "mongodb://localhost:27017/"

client = pymongo.MongoClient(uri)

db = client.infy

# collection="mycollection"

# mycol=db[collection]
db.create_collection("client")

client.close()
