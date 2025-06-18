from flask import Blueprint, jsonify, request
from src.services.movie_service import MovieService

movies_bp = Blueprint('movies', __name__)
service = MovieService()

@movies_bp.route('/movies', methods=['GET'])
def get_movies():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    filters = {
        'title': request.args.get('title'),
        'year': request.args.get('year'),
        'genre': request.args.get('genre')
    }
    return jsonify(service.get_movies(page, per_page, filters))

# ... otros endpoints