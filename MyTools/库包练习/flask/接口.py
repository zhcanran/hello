#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from flask import Flask, request, jsonify, send_file

app = Flask(__name__)  # 创建接口实例


# 第一个get请求的接口
@app.route('/hello')  # 创建路由，用户可以根据这个地址请求到下面的函数
def hello():
    return "hello flask"


# 第一个post请求的接口
@app.route('/hi', methods=['POST'])
def hi():
    return "hello flask"


# 第一个get or post请求的接口
@app.route('/h', methods=['POST', 'GET'])
def h():
    return "hello flask"


# 第一个get传参请求的接口
@app.route('/param')  # 创建路由，用户可以根据这个地址请求到下面的函数
def param():
    # data=request.args    #返回形式ImmutableMultiDict([('h', 'hello')]),适合get请求获取
    # data=request.form    #form表单的请求体，那么则可以使用request.form来获取参数。
    data = request.values  # 返回形式CombinedMultiDict([ImmutableMultiDict([('h', 'hello')])])
    print(data)
    dic = {'e': data['e'],
           'h': data['h']}
    return jsonify(dic)


# 第一个post传参请求的接口
@app.route('/param1', methods=['POST'])  # 创建路由，用户可以根据这个地址请求到下面的函数
def param1():
    data = request.form  # 获取表单数据

    # data = request.values  # 返回形式CombinedMultiDict([ImmutableMultiDict([('h', 'hello')])])
    print(data)
    dic = {'code': 200,
           'e': data['e'],
           'h': data['h']}
    return jsonify(dic)


# 第一个post上传文件接口
@app.route('/files', methods=['POST'])  # 创建路由，用户可以根据这个地址请求到下面的函数
def files():
    # data=request.form#咱是未获取到数据
    data = request.files['file']  # 返回形式CombinedMultiDict([ImmutableMultiDict([('h', 'hello')])])
    data.save(data.filename)  # 将获取的文件直接保存
    # print(data.filename)#获取文件名，可以对文件后缀，文件名等做校验工作
    dic = {'code': 200}
    return jsonify(dic)


# 第一个回传文件接口
@app.route('/downfiles', )
def downfiles():
    path = '张璨然1.jpg'
    return send_file(path)  # hui传的文件界面展示？


if __name__ == '__main__':
    host = '0.0.0.0'
    app.run(host=host, port=9000, debug=True)
