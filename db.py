
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
                query = "SELECT * from donor natural join blood"
                cursor.execute(query)

                data = cursor.fetchall()

                return render_template("deldonor.html", data=data)

        finally: conobj.close()
  elif option == 'delorg':
      return render_template('delorg.html')
  elif option == 'viewdonor':
      return render_template('viewwdonor.html')
  elif option == 'vieworg':
      return render_template('vieworg.html')
  else: return None



@app.route("/insert", methods = ['POST'])
def insert():

    username=request.form.get('username') #getting details from POST 
    password=request.form.get('password')
    sql="INSERT INTO  donor values(%s,%s,%s,%s,%s)"
    val=(request.form.get('did'),request.form.get('name'),request.form.get('age'),request.form.get('gender'),request.form.get('phone'))
    return query(username,password,sql,val)

@app.route("/dele", methods = ['POST'])
def dele():
    username=request.form.get('username')
    password=request.form.get('password')
    sql="DELETE FROM donor WHERE did = "+request.form.get('cond')
    val=None
    return query(username,password,sql,val)

def query(username,password,sql,val):

    try:
        conobj = mysql.connector.connect(host='localhost',
                                       database='db',
                                       user=username,
                                       password=password)
        if conobj.is_connected():
            cursor = conobj.cursor()
            cursor.execute(sql,val)
            conobj.commit()
    finally: conobj.close()
    return "a"


@app.route('/viewdonor', methods = ['POST'])       
def viewdonor():
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


if __name__ == "__main__":
    app.run()
 
# function ins(){
#   var name = $("#inname")[0].value;
#   var dno = $("#dno")[0].value;
#   send("ins",[name,dno]);
# }
# function del(){
#   var cond = $("#delcond")[0].value;
#   send("del",cond);
# }
# function upd(){
#   var cont = $("#updcont")[0].value;
#   var cond = $("#updcond")[0].value;
#   send("upd",[cont,cond]);
# }
# function send(query,params){
#   var qtype,d;
#   if(query==="upd"){
#     qtype = "/update";
#     d = {'uname':$("#uname")[0].value,
#       'pwd':$("#pwd")[0].value,
#       'cont':params[0],
#       'cond':params[1]};
#   }
#   if(query==="del"){
#     qtype = "/delete";
#     d = {'uname':$("#uname")[0].value,
#       'pwd':$("#pwd")[0].value,
#       'cond':params};
#   }
#   if(query==="ins"){
#     qtype = "/insert";
#     d = {'uname':$("#uname")[0].value,
#       'pwd':$("#pwd")[0].value,
#       'name':params[0],
#       'dno':params[1]};
#   }

#   $.ajax({
#     async: true,
#     type: "POST",
#     url: qtype,
#     data: d,
#     success: function(data){
#       var res = data['res'];
#       $("#response")[0].innerHTML="[ Response: "+res+" ]";
#     },
#     error: function(data){
#       $("#response")[0].innerHTML="Response: Login failure ]";
#     }
#   });
# }
