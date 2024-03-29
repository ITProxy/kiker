from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os
from config_loader import Config  # Импортируйте класс Config

config = Config() 
# Инициализация Flask-приложения
app = Flask(__name__)
app.config.update(config.get_flask_config()) # Задаем секретный ключ для сессий

# Конфигурация базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Определение моделей базы данных
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    # Дополнительные поля, как необходимо (например, ссылка на Telegram)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player1_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    player2_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score1 = db.Column(db.Integer, nullable=False)
    score2 = db.Column(db.Integer, nullable=False)
    # Дополнительные поля для турниров, даты и т.д.

# Маршруты и представления
@app.route('/')
def index():
    # Здесь будет логика для главной страницы
    return render_template('main.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Логика для формы входа
    if request.method == 'POST':
        # Обработка данных формы
        pass
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Логика для формы регистрации
    if request.method == 'POST':
        # Обработка данных формы
        pass
    return render_template('registration.html')

@app.route('/profile')
def profile():
    # Логика для личного кабинета пользователя
    return render_template('user_page.html')

@app.route('/submit_game', methods=['GET', 'POST'])
def submit_game():
    # Логика для страницы с результатами игры
    if request.method == 'POST':
        # Обработка данных формы
        pass
    return render_template('results.html')

# Запуск приложения
if __name__ == '__main__':
    server_config = config.get_server_config()
    app.run(debug=server_config['debug'], port=server_config['port'], host=server_config['host'])
