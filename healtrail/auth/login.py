from flask import request,url_for,redirect,render_template,session
from flask import Blueprint
from flask_mysqldb import MySQLdb,MySQL



mysql=MySQL()
signin=Blueprint('signin',__name__)
@signin.route("/signin",methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM sign_up WHERE email = %s",(email,))
        user=cur.fetchone()
        # if user:
        #     session['loggedin']=True
        #     session['user']= user['email']
        #     session['user_id']= user['id']
        return redirect(url_for('data_fetch.fetch'))
    else:
        pass
    return render_template('sign-in.html')