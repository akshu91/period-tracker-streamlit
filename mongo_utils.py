from pymongo import MongoClient

MONGO_URI = "mongodb+srv://backupakshu01:Ravi%401004@cluster0.kgp9l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["PeriodTracker"]
collection = db["UserData"]

def store_data(username, start_date, cycle_length, period_length):
    data = {
        "username": username,
        "start_date": start_date,
        "cycle_length": cycle_length,
        "period_length": period_length
    }
    collection.insert_one(data)

def get_history(username):
    return list(collection.find({"username": username}, {"_id": 0}))
