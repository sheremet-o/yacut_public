from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap


NO_REQUEST_BODY = 'Отсутствует тело запроса'
REQUIRED_URL = '\"url\" является обязательным полем!'
NAME_IS_OCCUPIED = 'Имя "{custom_id}" уже занято.'
INVALID_NAME_FOR_LINK = 'Указано недопустимое имя для короткой ссылки'
ID_NOT_FOUND = 'Указанный id не найден'


@app.route('/api/id/', methods=['POST'])
def create_id():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(NO_REQUEST_BODY)
    if 'url' not in data:
        raise InvalidAPIUsage(REQUIRED_URL)
    url_map = URLMap()
    custom_id = data.get('custom_id', None)

    if not custom_id or custom_id is None:
        custom_id = url_map.get_unique_short_id()
        data.update({'custom_id': custom_id})
    if url_map.is_short_link_exists(custom_id):
        raise InvalidAPIUsage(
            NAME_IS_OCCUPIED.format(custom_id=custom_id)
        )
    if not url_map.is_valid_short_id(custom_id):
        raise InvalidAPIUsage(INVALID_NAME_FOR_LINK)
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    url_map = URLMap.get_url_map(short_id)
    if not url_map:
        raise InvalidAPIUsage(ID_NOT_FOUND, 404)
    return jsonify({'url': url_map.original}), 200