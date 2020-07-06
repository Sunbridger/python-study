import flask, json
from flask import request

# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)
# server.config['JSON_AS_ASCII'] = False
# @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式
@server.route('/login', methods=['get', 'post'])
def login():
    # 获取通过url请求传参的数据
    username = request.values.get('name')
    # 获取url请求传的密码，明文
    pwd = request.values.get('pwd')
    # 判断用户名、密码都不为空，如果不传用户名、密码则username和pwd为None
    if username and pwd:
        if username=='xiaoming' and pwd=='111':
            resu = {'code': 200, 'message': '登录成功'}
            return resu
        else:
            resu = {'code': -1, 'message': '账号密码错误'}
            return resu
    else:
        resu = {'code': 10001, 'message': '参数不能为空！'}
        return resu

if __name__ == '__main__':
    server.run(debug=True, port=8888, host='0.0.0.0')
