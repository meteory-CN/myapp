#!/usr/bin/python
# coding=utf-8

from app import app
from flask import render_template, flash, redirect
from .form import LoginForm


@app.route('/')
@app.route('/index')
def index():
    title = u"shijun"
    post = {"username": "shijun", "usersex": 30, "commint": u"我是你爸爸爸爸"}, \
           {"username": "shijie", "usersex": 31, "commint": u"我是妈妈妈妈"}, \
           {"username": "chenxiaolu", "usersex": 55, "commint": u"我是你滴滴滴滴滴"}
    return render_template('index.html',
                           post=post,
                           title=title)


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
