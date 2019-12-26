from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
'''Flask Script扩展提供向Flask插入外部脚本的功能，包括运行一个开发用的服务器，
一个定制的Python shell，设置数据库的脚本，cronjobs，及其他运行在web应用之外的命令行任务；
使得脚本和系统分开；
Flask Script和Flask本身的工作方式类似，只需定义和添加从命令行中被Manager实例调用的命令；'''
from apps import app
from apps.model import db

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

'''
# 初始化映射仓库 （第一次用）
python manager.py db  init
# 生成映射脚本
python manager.py db migrate
# 映射 数据库
python manager.py db upgrade

'''
if __name__ == '__main__':
    manager.run()


