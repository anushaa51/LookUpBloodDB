import mysql.connector,sys
from mysql.connector import Error
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def loginPage():
    return render_template("index.html")

# @app.route('/cool_form')
# def cool_form():
#     if request.method == 'POST':
#         # do stuff when the form is submitted

#         # redirect to end the POST handling
#         # the redirect can be to the same route or somewhere else
#         return redirect(url_for('index'))

#     # show the form, it wasn't submitted
#     return render_template('cool_form.html')



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
    return render_template('fail.html')

@app.route("/select",methods = ['POST'])
def select():
  option = request.form.get('id')
  if option == 'insdonor':
      return render_template('insert.html')
  elif option == 'insorg':
      return render_template('insorg.html')


if __name__ == "__main__":
    app.run()
 
