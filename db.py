
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
        if username=='root' and password=='antechi':
            return render_template('select.html')
        elif username=='hospital' and password == 'h':
            return render_template('hospital.html')
        else: return render_template('fail.html')
    except:
        return render_template('fail.html')
    return render_template('fail.html')


@app.route("/home")
def home():
  return render_template('select.html')

@app.route("/upddonor",methods = ['POST'])
def upddonor():
    # username=request.form.get('username')
    # password=request.form.get('password')
    if request.form.get('type') == "name":
        val = [request.form.get('name'),request.form.get('did')]
        sql="UPDATE donor set name = ? WHERE d_id =  ?"

    elif request.form.get('type') == "phone":
        val = [request.form.get('phone'),request.form.get('did')]

        sql="UPDATE donor set phone = ? WHERE d_id =  ?"


    elif request.form.get('type') == "weight":
        val = [request.form.get('weight'),request.form.get('did')]

        sql="UPDATE donor set weight = ? WHERE d_id =  ?"

    elif request.form.get('type') == "org":
        val = [request.form.get('phone'),request.form.get('oid'),request.form.get('brid')]

        sql="UPDATE branch set br_phone = ? WHERE o_id = ? and br_id = ?"
    return query('root','antechi',sql,val)




@app.route("/orgbranchdel",methods = ['POST'])
def orgbranchdel():
    if request.form.get('type') == "org":
        val = [request.form.get('oid')]
        sql1 = "DELETE from blood where b_id in ( select b_id from blood_br where o_id = ? ) "
        sql2 = "DELETE from organization where o_id = ? "
    elif request.form.get('type') == "branch":
        val = [request.form.get('oid'),request.form.get('brid')]
        sql1 = "DELETE from blood where b_id in ( select b_id from blood_br where o_id = ? and br_id = ?) "
        sql2 = "DELETE from branch where o_id = ? and br_id = ?"

    try:
        conobj = mysql.connector.connect(host='localhost',
                                       database='db',
                                       user='root',
                                       password='antechi')
        if conobj.is_connected():
            cursor = conobj.cursor(prepared=True)
            cursor.execute(sql1,val)
            cursor.execute(sql2,val)
            conobj.commit()
    finally: conobj.close()
    return "a"


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
        try:
            conobj = mysql.connector.connect(host='localhost',
                                           database='db',
                                           user='root',
                                           password='antechi')
            if conobj.is_connected():
                cursor = conobj.cursor()
                query = "SELECT * from blood natural join blood_br"
                cursor.execute(query)

                data = cursor.fetchall()
                conobj.close()
                return render_template("deldonor.html", data=data)

        finally: conobj.close()
  elif option == 'orgdel':
      return render_template('orgdel.html')
  elif option == 'branchdel':
      return render_template('branchdel.html')
  elif option == 'viewdonor':
      return render_template('viewseldonor.html')
  elif option == 'vieworg':
      return render_template('viewselorg.html')
  else: return None



@app.route("/insert", methods = ['POST'])
def insert():
    username=request.form.get('username') #getting details from POST 
    password=request.form.get('password')
    sql2 ="INSERT INTO blood VALUES (?,?,?,?,?,?,?)"
    sql3 = "INSERT INTO blood_br values (?,?,?)"
    val2=[request.form.get('bid'),request.form.get('haemo'),request.form.get('wbc'),request.form.get('rbc'),request.form.get('pc'),request.form.get('date'),request.form.get('did')]
    val3=[request.form.get('bid'),request.form.get('oid'),request.form.get('brid')]

    if request.form.get('type') == 'insnew':
        sql1="INSERT INTO  donor values (?,?,?,?,?,?,?)"
        val1=[request.form.get('did'),request.form.get('name'),request.form.get('age'),request.form.get('gender'),request.form.get('bg'),request.form.get('phone'),request.form.get('weight')]
 
        try:
            conobj = mysql.connector.connect(host='localhost',
                                           database='db',
                                           user=username,
                                           password=password)
            if conobj.is_connected():
                cursor = conobj.cursor(prepared=True)
                cursor.execute(sql1,val1)
                cursor.execute(sql2,val2)
                cursor.execute(sql3,val3)
                conobj.commit()
        finally: conobj.close()
        return "a"
    elif request.form.get('type') == "insold":
      try:
            conobj = mysql.connector.connect(host='localhost',
                                           database='db',
                                           user=username,
                                           password=password)
            if conobj.is_connected():
                cursor = conobj.cursor(prepared=True)
                cursor.execute(sql2,val2)
                cursor.execute(sql3,val3)
                conobj.commit()
      finally: conobj.close()
      return "a"


@app.route("/dele", methods = ['POST'])
def dele():
    username=request.form.get('username')
    password=request.form.get('password')

    sql="DELETE FROM blood WHERE b_id = ?"
    val=[request.form.get('bid')]
    return query(username,password,sql,val)

def query(username,password,sql,val):

    try:
        conobj = mysql.connector.connect(host='localhost',
                                       database='db',
                                       user=username,
                                       password=password)
        if conobj.is_connected():
            cursor = conobj.cursor(prepared=True)
            cursor.execute(sql,val)
            conobj.commit()
    finally: conobj.close()
    return "a"


@app.route('/viewallblood', methods = ['POST'])       
def viewallblood():
    try:
        conobj = mysql.connector.connect(host='localhost',
                                       database='db',
                                       user='root',
                                       password='antechi')
        if conobj.is_connected():
            cursor = conobj.cursor()
            query = "SELECT * from donor natural join blood"
            cursor.execute(query)

            data = cursor.fetchall()

            return render_template("viewdonor.html", data=data)

    finally: conobj.close()
    return "a"

@app.route('/viewallorg', methods = ['POST'])       
def viewallorg():
    try:
        conobj = mysql.connector.connect(host='localhost',
                                       database='db',
                                       user='root',
                                       password='antechi')
        if conobj.is_connected():
            cursor = conobj.cursor()
            query = "SELECT * from organization"
            cursor.execute(query)

            data = cursor.fetchall()

            return render_template("viewallorg.html", data=data)

    finally: conobj.close()
    return "a"


@app.route('/viewanorg',methods = ['POST'])
def viewanorg():
    try:
        conobj = mysql.connector.connect(host='localhost',
                                       database='db',
                                       user='root',
                                       password='antechi')
        if conobj.is_connected():
            cursor = conobj.cursor()
            query = "SELECT org_name,br_id,address,br_phone from organization o natural join branch where o.o_id = " + '"' + request.form.get('oid') + '"'
            cursor.execute(query)

            data = cursor.fetchall()

            return render_template("viewanorg.html", data=data)

    finally: conobj.close()
    return "a"

@app.route('/viewbybg',methods = ['POST'])
def viewbybg():
    try:
        conobj = mysql.connector.connect(host='localhost',
                                       database='db',
                                       user='root',
                                       password='antechi')
        if conobj.is_connected():
            cursor = conobj.cursor()            
            query = "SELECT b_group,br.o_id,br.br_id,address,br_phone,dist from donor d, blood b,blood_br bbr,branch br,distance di where h_id = " + "'" + request.form.get('hid') + "'" + " and b_group = " + "'" + request.form.get('bg') + "'" + " and d.d_id = b.d_id and b.b_id = bbr.b_id and bbr.o_id = br.o_id and br.o_id = di.o_id and bbr.br_id = br.br_id and br.br_id = di.br_id order by (dist)"
            cursor.execute(query)

            data = cursor.fetchall()

            return render_template("viewbybg.html", data=data)

    finally: conobj.close()
    return "a"



if __name__ == "__main__":
    app.run()
