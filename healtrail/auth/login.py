from flask import request,url_for,redirect,render_template,session,flash
from flask import Blueprint
from flask_mysqldb import MySQLdb,MySQL
from flask_bcrypt import bcrypt



mysql=MySQL()
signin=Blueprint('signin',__name__)
@signin.route("/signin",methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        cur=mysql.connection.cursor()
        print(request.form)
        cur.execute("SELECT * FROM pharmacy_users WHERE email = %s and password_hash = %s",(email,password))
        user=cur.fetchone()
        print(user)
        if  user:
            session['loggedin']=True
            session['user']= user['email']
            session['user_id']= user['id']
           
        return redirect(url_for('data_fetch.fetch'))
    else:
      flash('Incorrect email or Password ')  
    return render_template('sign-in.html')

@signin.route("/logout",methods=['GET','POST'])
def logout():
    session.clear()
    return redirect(url_for('signin.login'))
