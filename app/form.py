from flask_wtf import Form
from wtforms import StringField,BooleanField,IntegerField
from wtforms.validators import DataRequired
class LoginForm(Form):
    openid = StringField('openid',validators=[DataRequired()])
    remember_me = BooleanField('remember_me',default=False)
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = 'a random string'