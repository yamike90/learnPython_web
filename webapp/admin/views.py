from flask import Blueprint, render_template

from webapp.user.decorators import admin_required

blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@blueprint.route('/')
@admin_required # декоратор для проверки аутентификации пользователя и админских прав на основе login_required из flask
def admin_index():
    title = 'Панель управления'
    return render_template('admin/index.html', page_title=title)
