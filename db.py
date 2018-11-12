import mysql.connector,sys
from mysql.connector import Error
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def loginPage():
    return render_template("index.html")


@app.route("/login", methods = ['POST'])
def login():
    username=request.form.get('username') 
    password=request.form.get('password')
    try:
        if username=='root' and password=='root':
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
    if request.form.get('type') == "orgaddr":
        sql1 = "SELECT count(*) from branch where o_id = ? and br_id = ?"
        val1 = [request.form.get('oid'),request.form.get('brid')]
        rowsmatched = count(sql1,val1)
        if rowsmatched > 0:
            val = [[request.form.get('hid1'),request.form.get('oid'),request.form.get('brid'),"H01"],[request.form.get('hid2'),request.form.get('oid'),request.form.get('brid'),"H02"],[request.form.get('hid3'),request.form.get('oid'),request.form.get('brid'),"H03"]]
            sql = "UPDATE distance set dist = ? where o_id = ? and br_id = ? and h_id = ?"
            sql2 = "UPDATE branch set address = ? where o_id = ? and br_id = ?"
            val2 = [request.form.get('addr'),request.form.get('oid'),request.form.get('brid')] 
            row = execQuery(sql2,val2)
            for q in val:
               execQuery(sql,q)
            return jsonify({'res':"Successfully updated!",
                       'rowsmatched':rowsmatched,
                       'rowsaffected':row
                      })

        else:
            return jsonify({
                       'rowsmatched':rowsmatched
                       })

    elif request.form.get('type') == "name":
        sql1 = "SELECT count(*) from donor where d_id = ?"
        val1 = [request.form.get('did')]
        rowsmatched = count(sql1,val1)
        # print(rowsmatched)
        if rowsmatched > 0:
            val = [request.form.get('name'),request.form.get('did')]
            sql="UPDATE donor set name = ? WHERE d_id =  ?"
            # rowsaffected = execQuery(sql,val)


    elif request.form.get('type') == "phone":
        sql1 = "SELECT count(*) from donor where d_id = ?"
        val1 = [request.form.get('did')]
        rowsmatched = count(sql1,val1)
        # print(rowsmatched)
        if rowsmatched > 0:
            val = [request.form.get('phone'),request.form.get('did')]
            sql="UPDATE donor set phone = ? WHERE d_id =  ?"
            # rowsaffected = execQuery(sql,val)


    elif request.form.get('type') == "weight":
        sql1 = "SELECT count(*) from donor where d_id = ?"
        val1 = [request.form.get('did')]
        rowsmatched = count(sql1,val1)
        if rowsmatched > 0:
            val = [request.form.get('weight'),request.form.get('did')]
            sql="UPDATE donor set weight = ? WHERE d_id =  ?"
            # rowsaffected = execQuery(sql,val)

    elif request.form.get('type') == "org":
        sql1 = "SELECT count(*) from branch where o_id = ? and br_id = ?"
        val1 = [request.form.get('oid'),request.form.get('brid')]
        rowsmatched = count(sql1,val1)
        if rowsmatched > 0:
            val = [request.form.get('phone'),request.form.get('oid'),request.form.get('brid')]
            sql="UPDATE branch set br_phone = ? WHERE o_id = ? and br_id = ?"
            # rowsaffected = execQuery(sql,val)

    elif request.form.get('type') == "orgname":
        sql1 = "SELECT count(*) from branch where o_id = ? and br_id = ?"
        val1 = [request.form.get('oid'),request.form.get('brid')]
        rowsmatched = count(sql1,val1)
        if rowsmatched > 0:
            val = [request.form.get('name'),request.form.get('oid')]
            sql="UPDATE organization set org_name = ? WHERE o_id = ?"
            # rowsaffected = execQuery(sql,val)

    if rowsmatched > 0:
        rowsaffected = execQuery(sql,val)
        return jsonify({'res':"Successfully updated!",
                       'rowsmatched':rowsmatched,
                       'rowsaffected':rowsaffected
                      })
    return jsonify({
                       'rowsmatched':rowsmatched,
                      })



@app.route("/orgbranchdel",methods = ['POST'])
def orgbranchdel():
    if request.form.get('type') == "org":
        val = [request.form.get('oid')]
        # sql1 = "DELETE from blood where b_id in ( select b_id from blood_br where o_id = ? ) "
        sql1 = "UPDATE blood_br set o_id ='GOV', br_id = 'DEF' where o_id = ? "
        sql2 = "DELETE from organization where o_id = ? "
    elif request.form.get('type') == "branch":
        val = [request.form.get('oid'),request.form.get('brid')]
        sql1 = "UPDATE blood_br set o_id ='GOV', br_id = 'DEF' where o_id = ? and br_id = ?"
        sql2 = "DELETE from branch where o_id = ? and br_id = ?"
    row = execQuery(sql1,val)
    execQuery(sql2,val)
    return jsonify(
                  {'res':"Blood entries moved to Bengaluru City Blood Bank : ",
                   'row':row
                  })



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
                                           password='root')
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

@app.route("/insertorg", methods = ['POST'])
def insertorg():
    username=request.form.get('username') #getting details from POST 
    password=request.form.get('password')
    sql1 = "INSERT into organization values (?,?,?)"
    sql2 = "INSERT into branch values (?,?,?,?)"
    sql3 = "INSERT into distance values (?,?,?,?)"
    val1 = [request.form.get('oid'),request.form.get('oname'),request.form.get('no')]
    val2 = [request.form.get('oid'),request.form.get('brid'),request.form.get('braddr'),request.form.get('brphno')]
    val3 = [[request.form.get('oid'),request.form.get('brid'),"H01",request.form.get('hid1')],[request.form.get('oid'),request.form.get('brid'),"H02",request.form.get('hid2')],[request.form.get('oid'),request.form.get('brid'),"H03",request.form.get('hid3')]]
    try:
            conobj = mysql.connector.connect(host='localhost',
                                           database='db',
                                           user=username,
                                           password=password)
            if conobj.is_connected():
                cursor = conobj.cursor(prepared=True)
                cursor.execute(sql1,val1)
                cursor.execute(sql2,val2)
                for q in val3:
                    cursor.execute(sql3,q)
                conobj.commit()
                return jsonify({'res': "SUCC"})
    except mysql.connector.errors.IntegrityError as err:
          # conobj.close()

          if err.errno == 1062:              #errorcode for both unique and primary key constraints
              return jsonify({'res': "PRI"})
          elif err.errno == 1452:            #errorcode for foreign key constraint
              return jsonify({'res': "FOR"})
          else:                              #handle any other mysql error
              return jsonify({'res': "UNK"})
    finally:conobj.close()


@app.route("/insertbranch", methods = ['POST'])
def insertbranch():
    username=request.form.get('username') #getting details from POST 
    password=request.form.get('password')
    sql1 = "INSERT into branch values (?,?,?,?)"
    val1 = [request.form.get('oid'),request.form.get('brid'),request.form.get('braddr'),request.form.get('brphno')]
    sql2 = "INSERT into distance values (?,?,?,?)"
    val2 = [[request.form.get('oid'),request.form.get('brid'),"H01",request.form.get('hid1')],[request.form.get('oid'),request.form.get('brid'),"H02",request.form.get('hid2')],[request.form.get('oid'),request.form.get('brid'),"H03",request.form.get('hid3')]]

    try:
            conobj = mysql.connector.connect(host='localhost',
                                           database='db',
                                           user=username,
                                           password=password)
            if conobj.is_connected():
                cursor = conobj.cursor(prepared=True)
                cursor.execute(sql1,val1)
                for q in val2:
                    cursor.execute(sql2,q)
                conobj.commit()
                return jsonify({'res': "SUCC"})
    except mysql.connector.errors.IntegrityError as err:
          # conobj.close()

          if err.errno == 1062:              #errorcode for both unique and primary key constraints
              return jsonify({'res': "PRI"})
          elif err.errno == 1452:            #errorcode for foreign key constraint
              return jsonify({'res': "FOR"})
          else:                              #handle any other mysql error
              return jsonify({'res': "UNK"})
    finally:conobj.close()

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
                cursor.execute("INSERT into dummy values('1')")
                conobj.commit()
                # conobj.close()
                return jsonify({'res': "SUCC"})
        except Error as err:
            # conobj.close()
            if err.errno == 1062:              #errorcode for both unique and primary key constraints
                return jsonify({'res': "PRI"})
            elif err.errno == 1452:            #errorcode for foreign key constraint
                return jsonify({'res': "FOR"})
            else:                              #handle any other mysql error
                return jsonify({'res': "UNK"})
        finally: conobj.close()

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
                cursor.execute("INSERT into dummy values('1')")

                conobj.commit()
                # conobj.close()
                return jsonify({'res': "SUCC"})
      except mysql.connector.errors.IntegrityError as err:
          # conobj.close()

          if err.errno == 1062:              #errorcode for both unique and primary key constraints
              return jsonify({'res': "PRI"})
          elif err.errno == 1452:            #errorcode for foreign key constraint
              return jsonify({'res': "FOR"})
          else:                              #handle any other mysql error
              return jsonify({'res': "UNK"})
      finally: conobj.close()

@app.route("/dele", methods = ['POST']) #deletes from display all blood 
def dele():
    username=request.form.get('username')
    password=request.form.get('password')

    sql="DELETE FROM blood WHERE b_id = ?"
    val=[request.form.get('bid')]
    execQuery(sql,val)
    return("None")



@app.route('/viewallblood', methods = ['POST'])       
def viewallblood():
    try:
        conobj = mysql.connector.connect(host='localhost',
                                       database='db',
                                       user='root',
                                       password='root')
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
                                       password='root')
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
                                       password='root')
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

    conobj = execView()
    cursor = conobj.cursor()            
    query = "SELECT b_group,br.o_id,br.br_id,address,br_phone,dist from donor d, blood b,blood_br bbr,branch br,distance di where h_id = " + "'" + request.form.get('hid') + "'" + " and b_group = " + "'" + request.form.get('bg') + "'" + " and d.d_id = b.d_id and b.b_id = bbr.b_id and bbr.o_id = br.o_id and br.o_id = di.o_id and bbr.br_id = br.br_id and br.br_id = di.br_id order by (dist)"
    cursor.execute(query)

    data = cursor.fetchall()
    conobj.close()

    return render_template("viewbybg.html", data=data)

def execQuery(sql,val):
  try:
      conobj = mysql.connector.connect(host='localhost',
                                           database='db',
                                           user='root',
                                           password='root')
      if conobj.is_connected():
          cursor = conobj.cursor(prepared=True)
          cursor.execute(sql,val)
          conobj.commit() 
          return cursor.rowcount       
  except Error as err:
          return err.errno
  finally: conobj.close()
  return None

def count(sql,val):
  try:
      conobj = mysql.connector.connect(host='localhost',
                                           database='db',
                                           user='root',
                                           password='root')
      if conobj.is_connected():
          cursor = conobj.cursor(prepared=True)
          cursor.execute(sql,val)
          result = cursor.fetchone()
          conobj.commit() 
          return result[0]      
  # except Error as err:
  #         return err.errno
  finally: conobj.close()
  return None

def execView():
    # username=request.form.get('username')
    # password=request.form.get('password')
    conobj = mysql.connector.connect(host='localhost',
                                       database='db',
                                       user='root',
                                       password='root')
    if conobj.is_connected():
        return conobj
    else: 
        return "a"


if __name__ == "__main__":
    app.run()

# def query(username,password,sql,val):

#     try:
#         conobj = mysql.connector.connect(host='localhost',
#                                        database='db',
#                                        user=username,
#                                        password=password)
#         if conobj.is_connected():
#             cursor = conobj.cursor(prepared=True)
#             cursor.execute(sql,val)
#             row = cursor.rowcount
#             conobj.commit()
                

#     finally: conobj.close()
#     return jsonify(
#                   {'res':" Updated entries : ",
#                    'row':row
#                   })
    



