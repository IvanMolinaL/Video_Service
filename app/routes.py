from flask import Blueprint, request, jsonify, current_app, send_file
from werkzeug.utils import secure_filename
from bson import ObjectId
from .gridfs_utils import GridFSUtils
from app.config import Config
import io

main = Blueprint('main', __name__)

# Instancia global de GridFSUtils
gridfs_utils = GridFSUtils(Config.MONGO_URI, "flask_video_service")

@main.route('/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    filename = secure_filename(file.filename)
    content_type = file.content_type
    file_id = gridfs_utils.upload_file(file, filename, content_type)
    return jsonify({'file_id': str(file_id)}), 201

@main.route('/download/<file_id>', methods=['GET'])
def download_video(file_id):
    try:
        file_id_obj = ObjectId(file_id)
        file_data, content_type = gridfs_utils.download_file(file_id_obj)
        return send_file(
            io.BytesIO(file_data),
            mimetype=content_type,
            as_attachment=True,
            download_name=f"{file_id}.mp4"
        )
    except Exception:
        return jsonify({'error': 'File not found'}), 404

@main.route('/videos', methods=['GET'])
def list_videos():
    # Aquí puedes implementar la lógica para listar videos
    return jsonify({'message': 'List of videos'}), 200