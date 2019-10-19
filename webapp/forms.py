from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField #импорт типов полей
from wtforms.validators import DataRequired #импорт валидатора - класс, который проверяет, что поля заполнены

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"}) #render_kw - использование готовых классов Bootstrap
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})
