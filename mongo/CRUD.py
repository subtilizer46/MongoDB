import pymongo

# Connect to the MongoDB server running locally
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or select a database
mydb = client["infy"]

# Create a collection (similar to a table in SQL)
mycol = mydb["menu"]

# Create (Insert) Operation
def create_document(data):
    mycol.insert_one(data)
    print("Document inserted successfully!")

# Read (Select) Operation
def read_documents():
    documents = mycol.find()
    for doc in documents:
        print(doc)

# Update Operation
def update_document(query, new_data):
    mycol.update_one(query, {"$set": new_data})
    print("Document updated successfully!")

# Delete Operation
def delete_document(query):
    mycol.delete_one(query)
    print("Document deleted successfully!")

# Menu for CRUD operations
def menu():
    while True:
        print("\nChoose an operation:")
        print("1. Create Document")
        print("2. Read Documents")
        print("3. Update Document")
        print("4. Delete Document")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == "1":
            new_customer = {
                "name": input("Enter name: "),
                "email": input("Enter email: "),
                "age": int(input("Enter age: "))
            }
            create_document(new_customer)
        elif choice == "2":
            read_documents()
        elif choice == "3":
            update_query = {"name": input("Enter the name of the document to update: ")}
            new_data = {
                "name": input("Enter new name: "),
                "email": input("Enter new email: "),
                "age": int(input("Enter new age: "))
            }
            update_document(update_query, new_data)
        elif choice == "4":
            delete_query = {"name": input("Enter the name of the document to delete: ")}
            delete_document(delete_query)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid option.")


menu()