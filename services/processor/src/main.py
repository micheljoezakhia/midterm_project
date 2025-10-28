from bs4 import BeautifulSoup
import pymongo

# -----------------------------
# 🔧 MongoDB Connection
# -----------------------------
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["scraper_db"]

raw_collection = db["scraped_data"]
clean_collection = db["clean_data"]

# -----------------------------
# 🧹 Data Cleaning Function
# -----------------------------
def clean_text(html):
    soup = BeautifulSoup(html, "lxml")
    # Remove script/style elements
    for tag in soup(["script", "style"]):
        tag.decompose()
    # Extract text only
    text = soup.get_text(separator=" ", strip=True)
    return text

# -----------------------------
# 🚀 Main Processor Logic
# -----------------------------
def process_data():
    count = 0
    for doc in raw_collection.find():
        if "html" in doc:  # if we have full HTML
            text = clean_text(doc["html"])
        elif "title" in doc:  # if we only have titles
            text = doc["title"]
        else:
            continue

        cleaned_doc = {
            "url": doc.get("url"),
            "clean_text": text,
            "timestamp": doc.get("timestamp")
        }
        clean_collection.insert_one(cleaned_doc)
        count += 1

    print(f"✅ Processed and cleaned {count} documents.")

if __name__ == "__main__":
    process_data()
