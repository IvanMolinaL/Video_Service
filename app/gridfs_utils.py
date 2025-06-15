from pymongo import MongoClient
import gridfs

class GridFSUtils:
    def __init__(self, mongo_uri, db_name):
        self.client = MongoClient(mongo_uri)
        print("Conectado a MongoDB en", mongo_uri)  # <-- Agrega esto
        self.db = self.client[db_name]
        self.fs = gridfs.GridFS(self.db)

    def upload_file(self, file_stream, filename, content_type):
        file_id = self.fs.put(file_stream, filename=filename, content_type=content_type)
        return file_id

    def download_file(self, file_id):
        file_data = self.fs.get(file_id)
        return file_data.read(), file_data.content_type

    def delete_file(self, file_id):
        self.fs.delete(file_id)

    def get_file_metadata(self, file_id):
        return self.fs.get(file_id).metadata