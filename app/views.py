#!/usr/bin/python
#coding=utf-8

from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    title = u"shijun"
    post = {"username": "shijun", "usersex": 30, "commint": u"我是你爸爸爸爸"}
    return render_template('index.html',
                           post=post,
                           title=title)
