import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# mydict = {"name": "John", "address": "Nowy nowy wpis"}

# x = mycol.insert_one(mydict)
# print(x.inserted_id)

print(mydb.list_collection_names())
print(myclient.list_database_names())

"""mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

# print list of the _id values of the inserted documents:
print(x.inserted_ids)"""

x = mycol.find_one()
print(x)

for x in mycol.find():
    print(x)


# for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
#    print(x)

# myquery = { "address": "Park Lane 38" }
# myquery = { "address": { "$gt": "S" } }
myquery = {"address": {"$regex": "^S"}}

mydoc = mycol.find(myquery)
mydoc = mycol.find().sort("name", -1)

# for x in mydoc:
#    print(x)


print(mycol.find().sort("_id", -1)[1])
