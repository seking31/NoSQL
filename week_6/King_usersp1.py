"""
Title: King_usersp1.py
Author: Sara King
Date: July 6, 2025
Description: Hands-On 6.1: Aggregate Queries
"""


from pymongo import MongoClient

client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.qxxmbuj.mongodb.net/?retryWrites=true&w=majority&appName=BellevueUniversity")

db = client["web335DB"]                 
collection = db["users"]               

print("All documents:")
for doc in collection.find():
    print(doc)

print(collection.find_one({"employeeId": 1011}))

print(collection.find_one({"lastName": "Mozart"}))
