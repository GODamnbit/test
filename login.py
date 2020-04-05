# coding=utf-8
import json
from flask import request, Blueprint
import op_db
from flask_cors import *

log_server = Blueprint('login', __name__)
CORS(log_server, resources=r'/*')


@log_server.route('/login', methods=['POST'])
def login():
    # 登录需要两个参数，user_id和pwd
    user_id_log = request.values.get('user_id')
    passwd_log = request.values.get('password')
    if user_id_log and passwd_log:  # 非空为真
        # 需要先写一个导入数据库的函数
        sql = "SELECT * FROM user WHERE user_id='%s' AND password='%s';" % (user_id_log, passwd_log)
        result = op_db.login_add(sql)  # 执行sql
        if result:
            res = {"error_code": 1000, "mag": "登录成功!"}  # 接口返回的都是json
        else:
            res = {"error_code": 3001, "mag": "账号或密码错误！"}
    else:
        res = {"error_code": 3000, "mag": "必填参数未填，请查看接口文档！"}

    return json.dumps(res, ensure_ascii=False)  # 防止出现乱码；json.dumps()函数是将字典转化为字符串
