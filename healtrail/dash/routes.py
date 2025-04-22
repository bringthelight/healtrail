from flask import request,url_for,redirect,render_template
from flask import Blueprint

dash=Blueprint('dash',__name__)
@dash.route('/')
def dashboard():
    return render_template('/dashboard.html')