#!/bin/python
# encoding:utf-8

from flask import Flask, request

app = Flask(__name__)


# app.route 修饰器
@app.route('/')
def index():
    return '<h1>Hello World</h1>'


# 动态参数
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s! </h1>' % name


# 上下文函数
@app.route('/idx')
def idx_view():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


# 查看URL映射
url_map = app.url_map
print(url_map)

if __name__ == '__main__':
    app.run(debug=True)  # 采用debug的方式启动
