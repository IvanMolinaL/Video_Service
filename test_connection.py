import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

try:
    client = pymongo.MongoClient(
        f"mongodb+srv://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@cluster0.szjwynp.mongodb.net/?retryWrites=true&w=majority",
        serverSelectionTimeoutMS=5000
    )
    print(client.server_info())
except Exception as e:
    print(f"Error: {e}")