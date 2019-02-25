#!/bin/python
# encoding:utf-8

from flask import Flask
# from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)


@app.route('/')
def index():
    # return '<h1>Bad Request</h1>', 400  # 状态码返回

    # 通过response对象进行返回
    # response = make_response('<h1>This document carries a cookie!</h1>')
    # response.set_cookie('answer', '42')
    # return response

    # 重定向
    return redirect('https://www.baidu.com')


# abort 函数 不会吧控制权交给调用她的函数
@app.route('/user/<id>')
def get_user(id):
    # 特殊的响应由abort函数处理
    if id == '1':
        abort(404)
    return '<h1>Hello, %s </h1>' % id


if __name__ == '__main__':
    app.run(debug=True)
