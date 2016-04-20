#!/usr/bin/python
# coding=utf-8

from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    title = u"shijun"
    post = {"username": "shijun", "usersex": 30, "commint": u"我是你爸爸爸爸"},\
           {"username": "shijie", "usersex": 31,"commint": u"我是妈妈妈妈"}, \
           {"username": "chenxiaolu","usersex": 55,"commint": u"我是你滴滴滴滴滴"}
    return render_template('index.html',
                           post=post,
                           title=title)
