import json
from models import db, User
from flask import Blueprint, request

delete_server = Blueprint('delete', __name__)


@delete_server.route('/delete', methods=['POST'])
def delete_user():
    user_id_dele = request.values.get("user_id")
    d_user = User.query.filter(User.user_id == user_id_dele).first()
    if d_user:
        db.session.delete(d_user)
        db.session.commit()
        res = {"error_code": 200, "msg": "删除成功！ "}
    else:
        res = {"error_code": 300, "msg": "删除失败！未找到该用户！ "}

    return json.dumps(res, ensure_ascii=False)  # 防止出现乱码
