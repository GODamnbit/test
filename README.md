���л�����python 3.7

����������װ��
������л�����ĿĿ¼��ִ��pip install -r requirements.txt

��Ŀִ�У�
�����ִ��python app.py

�ӿڲ��ԣ�
��Ŀ���к�ʹ��postman���ԣ�
1. ��¼���ԣ�POST  127.0.0.1��5000/login
	header��json����ֵ��user_id��password
	��ex��user_id��121��password��2w123��

2. ע����ԣ�POST  127.0.0.1:5000/add
	header��json����ֵ��user_id��phone��user_name��(email)��password��(sex)��born_date
	��ex��user_id��2��phone��126��user_name��lala��password��w123��sex���У�born_date��1999-2-3��
	ps�������ڲ�����Ϊ�գ�sex����/Ů

3. �������ԣ�POST  127.0.0.1��5000/by_station_name
	header��json����ֵ��station_name
	��ex��station_name������·��
	    
	    POST 127.0.0.1��5000/by_route
	header��json����ֵ��route_station_id
	��ex��route_station_id��1������Χ1-5��