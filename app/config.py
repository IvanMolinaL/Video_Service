import os

class Config:
    MONGO_URI = "mongodb://localhost:27017/"
    MONGO_DBNAME = "flask_video_service"
    GRIDFS_BUCKET = "videos"