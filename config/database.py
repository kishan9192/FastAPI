from pymongo.mongo_client import MongoClient

client = MongoClient(
    "mongodb+srv://admin:Admin123@cluster0.i0ikj5j.mongodb.net/?retryWrites=true&w=majority"
)


db = client.todo_list_db
collection_name = db["todo_collection"]
