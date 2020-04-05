# coding=utf-8
import json
import op_db
from flask import Blueprint, request
from models import db, User, User_bus, User_passenger, User_station
from flask_cors import *


add_server = Blueprint('add', __name__)
CORS(add_server, resources=r'/*')


@add_server.route('/add', methods=['POST'])
def add():
    user_id_log = request.values.get("user_id")
    phone = request.values.get("phone")
    user_name = request.values.get("user_name")
    email = request.values.get("email")
    password = request.values.get("password")
    sex = request.values.get("sex")
    if sex:
        if sex == '男':
            sex = 1
        elif sex == '女':
            sex = 0
    else:
        sex = 1
    birth = request.values.get("born_date")

    if user_id_log and phone and user_name and password and birth:  # 必填参数校验

        if not user_id_log.isdigit():  # 判断ID号格式是否正确
            res = {"error_code": 3006, "msg": "ID号输入错误"}

        else:
            sql = "select* from user where user_id='%s';" % user_id_log  # 查看数据库中是否有这个ID号，有的话说明重复
            result = op_db.login_add(sql)  # 执行sql
            if result:
                res = {"error_code": 1000, "msg": "ID号已经存在!"}

            else:
                sql = "INSERT INTO user(user_id, phone, user_name, email, password, sex, born_date)" \
                      "VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s')" \
                      % (user_id_log, phone, user_name, email, password, sex, birth)
                op_db.login_add(sql)
                # user_add = User(user_id=user_id_log, phone=phone, user_name=user_name, email=email, password=password,
                #                 sex=sex, born_date=birth)
                # db.session.add(user_add)
                # db.session.commit()
                res = {"error_code": 200, "msg": "新增成功！ "}
    else:
        res = {"error_code": 3007, "msg": "必填参数未填写!"}
    return json.dumps(res, ensure_ascii=False)  # 防止出现乱码
