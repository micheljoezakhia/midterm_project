import pymongo

try:
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["scraper_db"]
    test_collection = db["test_data"]
    test_collection.insert_one({"test": "connection_ok"})
    print("✅ Connected successfully and inserted test document.")
except Exception as e:
    print("❌ Connection failed:", e)
