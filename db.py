import mysql.connector,sys
from mysql.connector import Error
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def mainPage():
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
    uname=request.form.get('username') #getting details from POST 
    pwd=request.form.get('password')
    try:
        conobj = mysql.connector.connect(host='localhost',
                                       database='db',
                                       user=uname,
                                       password=pwd)
        if conobj.is_connected():
            return jsonify({"res" : "Success"})
    except Error as e:
        return jsonify({"res" : e.args[1]})
    #finally:
        #conobj.close()
    return jsonify({"res" : "failed to connect to MySQL"})






if __name__ == "__main__":
    app.run()
 
