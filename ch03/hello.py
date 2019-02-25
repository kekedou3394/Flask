#!/bin/python
# encoding:utf-8

from flask import Flask, render_template

app = Flask(__name__)


# app.route 修饰器
@app.route('/')
def index():
    return render_template('index.html')


# 动态参数
@app.route('/user/<name>')
def user(name):
    lgr = "User's name is {}".format(name)
    print(lgr)
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)  # 采用debug的方式启动
