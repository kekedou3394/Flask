#!/bin/python
# encoding:utf-8

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
# 20190227 初始化bootstrap
bootstrap = Bootstrap(app)


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


# 20190302 自定义错误页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)  # 采用debug的方式启动
