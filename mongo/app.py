import pymongo
from bson.objectid import ObjectId

uri = "mongodb://localhost:27017/"

client = pymongo.MongoClient(uri)

db = client.infy

collection = db.employee

if db is not None:
    print("Connected")

print(client.list_database_names())

print(db.list_collection_names())


data = {
    "name": "Rahul Singh",
    "age": 22,
    "email": "rs@gmail.com"
}

insert = collection.insert_one(data)

data = {"_id": ObjectId('6524faba8f85d129c34cc23d')}

phndata = {"_id": ObjectId('6523daa92f930d40eab6a621')}

dataup = {"_id": ObjectId('6523daba2f930d40eab6a623')}

criteria = {"_id": ObjectId('6523d1bf441bd18cba472688')}

newdata = {"_id": ObjectId('6523d1bf441bd18cba472688')}

update_data = {
    "$set": {
        "employees.0.first_name": "Rahul"
    }
}

update_newdata = {
    "$set": {
        "employees.3.first_name": "Sahil",
        "employees.3.last_name": "Singh",
        "employees.3.email": "sahil@yahoo.com",
        "employees.3.city": "Patna"
    }
}

update_phn_data = {
    "$set": {
        "phone": 8765465635
    }
}

documents = [
    {
        "first_name": "R",
        "last_name": "Singh",
        "email": "rks@yahoo.com",
        "phone": "76564673",
        "department": "IT",
        "position": "Manager",
        "salary": 40000
    },
    {
        "first_name": "S",
        "last_name": "Singh",
        "email": "ss@yahoo.com",
        "phone": "111111111",
        "department": "Marketing",
        "position": "Marketing",
        "salary": 50000
    }
]

del_data = {
    "$unset": {
        "position": 1
    }
}

result6 = collection.insert_many(documents)

result7 = collection.update_one(data, del_data)

update = {"$set": {"name": "Rohit Singh", "age": 20}}

result1 = collection.update_one(dataup, update)

result3 = collection.update_one(criteria, update_data)

result4 = collection.update_one(phndata, update_phn_data)

result5 = collection.update_one(newdata, update_newdata)

# result2 = collection.delete_one(data)

cursor = collection.find({})

for document in cursor:
    print(document)

client.close()



# from flask import Flask

# app = Flask(__name__)

# @app.route('/book/<int:num>', methods=['GET', 'POST'])
# def book(num):
#     if num==3:
#         return "i am in restaurant 3"
#     return f"Booking restaurant with ID: {num}"

# if __name__ == '__main__':
#     app.run(debug=True)