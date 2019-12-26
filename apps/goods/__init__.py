from flask import Blueprint

goods = Blueprint('goods', __name__)

from apps.goods import views
