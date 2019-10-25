from getpass import getpass # безопасный input
import sys # работа с системными функциями, будет использована для корректного завершения работы

from webapp import create_app
from webapp.model import db, User

app = create_app()

with app.app_context(): # контекст необходим для локальной работы БД
    username = input('Введите имя: ')

    if User.query.filter(User.username == username).count(): # проверка существования пользователя (возвращает количество совпадений в БД)
        print('Пользователь с таким именем уже существует')
        sys.exit(0) # выход из программы

    password1 = getpass('Веедите пароль: ')
    password2 = getpass('Повторите пароль: ')

    if not password1 == password2:
        print('Пароли не одинаковые')
        sys.exit(0)
    
    new_user = User(username = username, role = 'admin')
    new_user.set_password(password1) # использование метода set_password класса User

    db.session.add(new_user)
    db.session.commit()
    print('Создан пользователь с id = {}'.format(new_user.id))
