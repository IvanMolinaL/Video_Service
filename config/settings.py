import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = f"mongodb+srv://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@{os.getenv('MONGODB_HOST')}/{os.getenv('MONGODB_DB_NAME')}?retryWrites=true&w=majority"
    DB_NAME = os.getenv('MONGODB_DB_NAME')
    COLLECTION_NAME = "movies"