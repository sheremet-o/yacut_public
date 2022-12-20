from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import (DataRequired, Length, Optional, Regexp,
                                ValidationError)

from .models import URLMap

LINK_REG = r'^[a-zA-Z\d]{1,16}$'


class URLmapForm(FlaskForm):
    original_link = URLField(
        'Введите ссылку', validators=[
            DataRequired(message='Обязательное поле')])
    custom_id = StringField(
        'Ваш вариант короткой ссылки', validators=[
            Length(1, 16), Optional(), Regexp(
                regex=LINK_REG,
                message='Можно использовать большие и маленькие латинские буквы,а также цифры в диапазоне от 0 до 9.')])
    submit = SubmitField('Создать')

    def validate_custom_id(self, field):
        if field.data and URLMap.query.filter_by(short=field.data).first():
            raise ValidationError(f'Имя {field.data} уже занято!')