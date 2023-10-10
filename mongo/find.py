import pymongo

mongo_uri = "mongodb://localhost:27017/"
database_name = "infy"
collection_name = "employee"

client = pymongo.MongoClient(mongo_uri)
db = client[database_name]
collection = db[collection_name]



query = {"age": {"$gte": 18}}
projection = {"name": 1, "age": 1}
result = collection.find(query, projection)
for document in result:
    print(document)

print("###################################################################################################")

query1 = {"name": "Rohit Singh"}  
result1 = collection.find(query1)
for document1 in result1:
    print(document1)

print("###################################################################################################")

query2 = {"age": {"$gte": 21}}  
projection2 = {"name": 1, "age": 1} 
result2 = collection.find(query2, projection2)
for document2 in result2:
    print(document2)

print("###################################################################################################")

result3 = collection.find().sort("age", pymongo.ASCENDING)  
for document3 in result3:
    print(document3)

print("###################################################################################################")

result4 = collection.find().limit(5).skip(10)
for document4 in result4:
    print(document4) 

print("###################################################################################################")

query5 = {"$or": [{"name": "Rahul Singh"}, {"name": "Rohit Singh"}]}  
result5 = collection.find(query5)
for document5 in result5:
    print(document5) 

print("###################################################################################################")

import re
query6 = {"name": {"$regex": re.compile("^R")}}  
result6 = collection.find(query6)
for document6 in result6:
    print(document6) 

client.close()