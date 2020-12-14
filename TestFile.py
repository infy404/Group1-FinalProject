import pymongo

client = pymongo.MongoClient("mongodb+srv://ShrijanK:dummyPassword1234@cluster0.wfpuf.mongodb.net/DprogDb?retryWrites=true&w=majority")

myDb = client["DprogDb"]

data = {"Date": "Total Cases"}

val = myDb["Ontario"].find({}, {"_id": 0})


for txt in val:
    pair = [v for k, v in txt.items()]
    print(pair)


# print(data)
