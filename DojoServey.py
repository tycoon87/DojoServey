from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user',methods=['POST'])
def render():
    username = request.form['username']
    email = request.form['Email']
    location = request.form['DojoLocation']
    language = request.form['Favoreitelanguage']
    discription = request.form['discription']
    return render_template("user.html")

@app.route('/post')
def post():
    print "username {} <br> Email: {} <br> Dojo Location {} <br> Your favorate Language {} <br> Comments {}".format(username,email,location,language,request)

app.run(debug=True)