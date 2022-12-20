# Описание  

Yacut - сервис укорачивания ссылок с web интерфейсом и REST API. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Стек технологий  

* Python
* Flask
* Flask-SQLAlchemy
* Jinja
* Flask-WTF
* Flask-Migrate

## Запуск

1. Склонируйте репозиторий 
`git clone https://github.com/sheremet-o/yacut`  

2. Создайте и активируйте виртуальное окружение:  
`python -m venv .env`  
`source .env/Scripts/activate`  

3. Установите зависимости:
`pip install -r requirements.txt`  

4. Примените миграции  
`flask db upgrade`  

5. Запустите сервер  
`flask run`  
web интервейс будет доступен по адресу http://localhost:5000/

## Над проектом работали

Оксана Шеремет 