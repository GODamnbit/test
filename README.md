运行环境：python 3.7

依赖环境安装：
命令窗口切换到项目目录，执行pip install -r requirements.txt

项目执行：
命令窗下执行python app.py

接口测试：
项目运行后使用postman测试：
1. 登录测试：POST  127.0.0.1：5000/login
	header：json，键值对user_id、password
	（ex：user_id：121，password：2w123）

2. 注册测试：POST  127.0.0.1:5000/add
	header：json，键值对user_id、phone、user_name、(email)、password、(sex)、born_date
	（ex：user_id：2，phone：126，user_name：lala，password：w123，sex：男，born_date：1999-2-3）
	ps：括号内参数可为空，sex：男/女

3. 发布测试：POST  127.0.0.1：5000/by_station_name
	header：json，键值对station_name
	（ex：station_name：春熙路）
	    
	    POST 127.0.0.1：5000/by_route
	header：json，键值对route_station_id
	（ex：route_station_id：1）（范围1-5）