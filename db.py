
import mysql.connector,sys
from mysql.connector import Error
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def loginPage():
    return render_template("index.html")


@app.route("/login", methods = ['POST'])
def login():
    username=request.form.get('username') #getting details from POST 
    password=request.form.get('password')
    try:
        conobj = mysql.connector.connect(host='localhost',
                                       database='db',
                                       user=username,
                                       password=password)
        if conobj.is_connected():
            return render_template('select.html')
    except Error as e:
        return render_template('fail.html')
    finally: conobj.close()
    return render_template('fail.html')





@app.route("/select",methods = ['POST'])
def select():
  option = request.form.get('id')
  if option == 'insdonor':
      return render_template('insert.html')
  elif option == 'insorg':
      return render_template('insorg.html')
  elif option == 'upddonor':
      return render_template('upddonor.html')
  elif option == 'updorg':
      return render_template('updorg.html')
  elif option == 'deldonor':
      return render_template('deldonor.html')
  elif option == 'delorg':
      return render_template('delorg.html')
  elif option == 'viewdonor':
      return render_template('viewdonor.html')
  elif option == 'vieworg':
      return render_template('vieworg.html')



@app.route("/insert", methods = ['POST'])
def insert():

    username=request.form.get('username') #getting details from POST 
    password=request.form.get('password')
    sql="INSERT INTO  donor values(%s,%s,%s,%s,%s)"
    val=(request.form.get('did'),request.form.get('name'),request.form.get('age'),request.form.get('gender'),request.form.get('phone'))
    return query(username,password,sql,val)


def query(username,password,sql,val):

    try:
        conobj = mysql.connector.connect(host='localhost',
                                       database='db',
                                       user='root',
                                       password='antechi')
        if conobj.is_connected():
            cursor = conobj.cursor()
            cursor.execute(sql,val)
            conobj.commit()
    finally: conobj.close()
    return "a"


if __name__ == "__main__":
    app.run()
 
 
