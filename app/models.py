from mongoengine import Document, StringField, DateTimeField, FileField
from datetime import datetime

class Video(Document):
    title = StringField(required=True)
    description = StringField()
    upload_date = DateTimeField(default=datetime.utcnow)
    filename = StringField(required=True)
    content_type = StringField(required=True)
    length = StringField(required=True)  # Length of the video in seconds
    user_id = StringField(required=True)  # ID of the user who uploaded the video

    def __str__(self):
        return f"{self.title} ({self.filename})"