from flask_login import UserMixin # необходимый для работы класс flask-login c обязательными методами для работы модуля
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash # односторонне шифрование паролей

db = SQLAlchemy()

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<News {} {}>'.format(self.title, self.url)

class User(db.Model, UserMixin): #множественное наследование от классов db.Model и UserMixin
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(10), index=True)

    def set_password(self, password): # преобразовать пароль пользователя в хеш и сохранить в БД в таком виде
        self.password = generate_password_hash(password)

    def check_password(self, password): # сравнение хешей пароля из БД и введенного пользователем
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username) # при вызове функции возврат строки с именем пользователя, а не объекта
