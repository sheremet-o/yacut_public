import string
import re


# Constants for models.py
VALID_SYMBOLS = string.ascii_letters + string.digits
SYMBOLS_LENGTH = 6
USER_INPUT_LIMIT = 16

# API Error messages for api_views.py
NO_REQUEST_BODY = 'Отсутствует тело запроса'
REQUIRED_URL = '"url" является обязательным полем!'
ID_NOT_FOUND = 'Указанный id не найден'
NAME_IS_OCCUPIED = 'Имя "{custom_id}" уже занято.'
INVALID_NAME_FOR_LINK = 'Указано недопустимое имя для короткой ссылки'

# Flash messages for views.py
NAME_IS_OCCUPIED_FLASH = 'Имя {custom_id} уже занято!'
INVALID_SYMBOLS = f"""Заданная вами ссылка содержит недопустимые символы.
                      Разрешенные символы: {VALID_SYMBOLS}"""

PATTERN = f'[{re.escape(string.ascii_letters + string.digits)}]'