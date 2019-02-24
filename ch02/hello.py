#!/bin/python
# encoding:utf-8

from flask import Flask

app = Flask(__name__)


# app.route 修饰器
@app.route('/')
def index():
    return '<h1>Hello World</h1>'


# 动态参数
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s! </h1>' % name


if __name__ == '__main__':
    app.run(debug=True)  # 采用debug的方式启动
