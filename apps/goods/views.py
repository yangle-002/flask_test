from flask import render_template

from apps.goods import goods

@goods.route('/index')
def index():
    # return 'yangle'
    # return render_template('index.html',msg='我是小希')
    return render_template('index.html',m ={'msg':'我是小希1'})