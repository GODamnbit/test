# coding=utf-8
from flask import render_template, request, Blueprint, flash, url_for, redirect
import op_db
from datetime import datetime
from models import Route, Route_station
from flask_cors import *

fa = Blueprint('fabu', __name__)
CORS(fa, resources=r'/*')


@fa.route('/by_station_name', methods=['GET', 'POST'])  # 按站点名查询
def by_station_name():
    now = datetime.now()
    station_name = request.values.get('station_name')
    sql = "SELECT density FROM station WHERE station_name='%s';" % station_name
    results = op_db.fabu(sql).values()  # 执行sql
    for result in results:
        print(result[0])
        if result == "R":
            context1 = {
                'msg': station_name + '\n' + str(now) + '\n该站点人群密集！不建议由此站点出行！'
            }
            return render_template('by_station_name.html', image='./static/images/R.jpg', **context1)
        elif result == "B":
            context2 = {
                'msg': station_name + '\n' + str(now) + '\n该站点人群不怎么多，可考虑由此站点出行。'
            }
            return render_template('by_station_name.html', image='./static/images/B.jpg', **context2)
        elif result == "G":
            context3 = {
                'msg': station_name + '\n' + str(now) + '\n该站点人很少，很建议由此站点出行哦~'
            }
            return render_template('by_station_name.html', image='./static/images/G.jpg', **context3)


@fa.route('/by_route', methods=['GET', 'POST'])  # 按路线查询
def by_route():
    # route_name_input = request.values.get('route_name')
    station_id_input = request.values.get('route_station_id')
    # res_name = Route.query.filter(Route.route_name == route_name_input).first()
    # if res_name:
    #     context1 = {
    #         'msg': res_name + '该站点人群密集！不建议由此站点出行！'
    #     }
    #     return render_template('by_route.html', image='./static/images/sub_1.jpg', **context1)
    sql = "SELECT station_order FROM route_station WHERE route_station_id='%s';" % station_id_input
    results = op_db.fabu(sql).values()  # 执行sql
    for result in results:
        # print(result[0])
        if result == 1:
            context1 = {
                'msg': '\n该站点人群密集！不建议由此站点出行！'
            }
            return render_template('by_route.html', image='./static/images/sub_1.jpg', **context1)
        elif result == 2:
            context2 = {
                'msg': '\n该站点人群不怎么多，可考虑由此站点出行。'
            }
            return render_template('by_route.html', image='./static/images/sub_2.jpg', **context2)
        elif result == 3:
            context3 = {
                'msg': '\n该站点人很少，很建议由此站点出行哦~'
            }
            return render_template('by_route.html', image='./static/images/sub_3.jpg', **context3)


# @fa.route('/station', methods=['GET', 'POST'])
# def station_index():
#     context = {
#         'msg': '这里是人群密度查询首页，请选择您的查询方式。'
#     }
#     choose = request.values.get('query_way')
#     if choose == '站点查询':
#         return redirect(url_for("by_station_name"))
#     elif choose == '路线查询':
#         return redirect(url_for("by_route"))
#     return render_template('index.html', **context)
