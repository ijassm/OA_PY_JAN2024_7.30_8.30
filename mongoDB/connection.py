from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from bson import ObjectId


userName = "Enter your username"
password = "Enter your password"

uri = f"mongodb+srv://{userName}:{password}@python.lvsvs4f.mongodb.net/?retryWrites=true&w=majority&appName=PYTHON"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client["PY_JAN2024_7_8"]

students = db["students"]

# Create

# student = {
#     "firstName": "Merwin",
#     "lastName": "J",
#     "age": 18,
#     "gender": "Male",
#     "address": {
#         "city": "Puducherry",
#         "state": "Puducherry",
#         "country": "India",
#     },
#     "countryCode": "+91",
#     "phoneNumber": 8072937416,
#     "skills": [
#         {
#             "name": "PYTHON",
#             "level": 8,
#         },
#         {
#             "name": "C",
#             "level": 6,
#         },
#         {
#             "name": "C++",
#             "level": 7,
#         },
#     ],
#     "createdAt": datetime.datetime.now(),
# }


# students.insert_one(student)

# data = [
#     {
#         "firstName": "Sophia",
#         "lastName": "H",
#         "age": 22,
#         "gender": "Female",
#         "address": {"city": "Hyderabad", "state": "Telangana", "country": "India"},
#         "countryCode": "+91",
#         "phoneNumber": 8442567932,
#         "skills": [
#             {"name": "JAVASCRIPT", "level": 8},
#             {"name": "PYTHON", "level": 7},
#             {"name": "C", "level": 5},
#         ],
#         "createdAt": datetime.datetime.now(),
#     },
#     {
#         "firstName": "Emma",
#         "lastName": "I",
#         "age": 25,
#         "gender": "Female",
#         "address": {"city": "Delhi", "state": "Delhi", "country": "India"},
#         "countryCode": "+91",
#         "phoneNumber": 7198346205,
#         "skills": [
#             {"name": "C", "level": 9},
#             {"name": "PYTHON", "level": 8},
#             {"name": "GO", "level": 7},
#         ],
#         "createdAt": datetime.datetime.now(),
#     },
# ]

# create many

# students.insert_many(data)

# Read one

# student = students.find_one({"_id": ObjectId("666afe13d37672886d33bc0c")})

# print(student["skills"])


# Read all

# query = {
#     "gender": "Female",
# }

# filter = {"address": 1, "skills": 1, "_id": 0}

# student = students.find(query, filter)

# print(list(student))


print(db.list_collection_names())
