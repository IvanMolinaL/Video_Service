from bson import ObjectId, json_util
import json
from src.utils.database import get_db


class MovieService:
    def __init__(self):
        self.db = get_db()
        self.collection = self.db.movies

    def get_movies(self, page, per_page, filters):
        query = self._build_query(filters)
        skip = (page - 1) * per_page
        movies = list(self.collection.find(query).skip(skip).limit(per_page))
        total = self.collection.count_documents(query)

        return {
            "data": self._parse_json(movies),
            "pagination": {
                "page": page,
                "per_page": per_page,
                "total": total
            }
        }

    def _build_query(self, filters):
        query = {}
        if filters['title']:
            query['title'] = {"$regex": filters['title'], "$options": "i"}
        # ... otros filtros
        return query

    def _parse_json(self, data):
        return json.loads(json_util.dumps(data))