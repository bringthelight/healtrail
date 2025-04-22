from flask import request,url_for,redirect,render_template
from flask import Blueprint
from flask_mysqldb import MySQLdb,MySQL


auth=Blueprint('auth',__name__)
mysql=MySQL()
@auth.route('/signup',methods=['GET','POST'])
def signup():
    cur=mysql.connection.cursor()
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        cur.execute("INSERT INTO sign_up(name,email,password) VALUES(%s,%s,%s)",(name,email,password))
        mysql.connection.commit()
        
        
        return(redirect(url_for('dash.dashboard')))
    
    
    return render_template('auth/sign-up.html')



