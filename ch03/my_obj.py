#!/bin/python
# encoding:utf-8


# 定义一个对象，目的是验证Jinja2模版支持对象方法的读取
class MyObj:

    def __init__(self):
        print('my object =====')

    def somemethod(self):
        return 'Hello World , My Object'
