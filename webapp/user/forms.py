from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField #импорт типов полей
from wtforms.validators import DataRequired, Email, EqualTo #импорт валидатора - класс, который проверяет, что поля заполнены

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"}) #render_kw - использование готовых классов Bootstrap
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={"class": "form-check-input"}) # чек-бокс, подсмотренный в документации bootstrap
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})

class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    email = StringField('Электронная почта', validators=[DataRequired(), Email()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    password2 = PasswordField('Пароль', validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})
