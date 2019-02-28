#!/bin/python
# encoding:utf-8

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from ch03.my_obj import MyObj

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


@app.route('/sup')
def supJinja():
    # 字典
    mydict = {'key': 'WY'}
    # 列表
    mylist = [1, 2, 3, 4]
    myintvar = 2
    print(mydict)
    myobj = MyObj()

    return render_template('sup.html', mydict=mydict, mylist=mylist, myintvar=myintvar, myobj=myobj)


if __name__ == '__main__':
    app.run(debug=True)  # 采用debug的方式启动
