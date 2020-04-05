from flask import Flask
import add
import delete_user
import login
import fabu
import config
from exts import db
from flask_cors import *


# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(config)  # 配置文件实例化
#     app.register_blueprint(login.log_server)
#     app.register_blueprint(add.add_server)
#     app.register_blueprint(fabu.fa)
#     app.register_blueprint(delete_user.delete_server)
#     db.init_app(app)
#     return app


app = Flask(__name__)
app.config.from_object(config)  # 配置文件实例化
app.register_blueprint(login.log_server)
app.register_blueprint(add.add_server)
app.register_blueprint(fabu.fa)
CORS(app, resources=r'/*')


@app.route('/')
def index():
    return '这是首页！'


if __name__ == '__main__':
    # app = create_app()
    app.run(debug=True)
