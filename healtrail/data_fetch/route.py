from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from flask_mysqldb import MySQLdb,MySQL

mysql=MySQL()
data_fetch= Blueprint('data_fetch',__name__)

@data_fetch.route('/fetch',methods=['GET','POST'])
def fetch():
    cur= mysql.connection.cursor()
    
    
    cur.execute("SELECT * FROM master_unit")
    data = cur.fetchall()
    return render_template('medicine_unit.html', data=data)

@data_fetch.route()
