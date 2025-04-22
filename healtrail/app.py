from flask import Flask,session
from flask_session import Session
from auth.routes import auth
from auth.login import signin
from dash.routes import dash
from flask_mysqldb import MySQL
from data_fetch.route import data_fetch
from action.edit import edit
app=Flask(__name__,template_folder='templates/',static_folder='static/',static_url_path='/')

app.register_blueprint(auth)
app.register_blueprint(dash)
app.register_blueprint(data_fetch)
app.register_blueprint(signin)
app.register_blueprint(edit)
mysql=MySQL(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'healtrail_pharmacy'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SESSION_PERMANENT']= False
app.config["SESSION_TYPE"]="filesystem"

Session(app)




if __name__=='__main__':
    app.run(debug=True)