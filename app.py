from flask import Flask, jsonify, request
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
from dotenv import load_dotenv
from bson import json_util, ObjectId
import json

# Configuración Flask
app = Flask(__name__)

# Conexión MongoDB
load_dotenv()

try:
    MONGO_URI = f"mongodb+srv://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@cluster0.szjwynp.mongodb.net/{os.getenv('MONGODB_DB_NAME')}?retryWrites=true&w=majority&appName=VideoService"
    client = MongoClient(MONGO_URI)
    db = client[os.getenv('MONGODB_DB_NAME')]  # Ahora usará sample_mflix
    collection = db['movies']  # Colección correcta
    print("✅ Conexión exitosa a MongoDB Atlas")
    print(f"Colecciones disponibles: {db.list_collection_names()}")  # Para diagnóstico
except ConnectionFailure as e:
    print(f"❌ Error de conexión: {e}")
    exit(1)


# Helper para JSON
def parse_json(data):
    return json.loads(json_util.dumps(data))


# Rutas
@app.route('/movies', methods=['GET'])
def get_movies():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))

        movies = list(collection.find().skip((page - 1) * per_page).limit(per_page))
        return jsonify({
            "data": parse_json(movies),
            "page": page,
            "per_page": per_page,
            "total": collection.count_documents({})
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/movies/<string:movie_id>', methods=['GET'])
def get_movie(movie_id):
    try:
        movie = collection.find_one({"_id": ObjectId(movie_id)})
        if movie:
            return parse_json(movie)
        return jsonify({"error": "Movie not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)