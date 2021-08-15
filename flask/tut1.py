from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") # this is like url / is the kind of the rootpage
def hello_world():
    return render_template('index.html')

@app.route("/about") # this is the /about page url = 127.0.0.1:5000/about
def pews():
    return render_template('about.html')

@app.route("/npews") # # this is the /npews page url = 127.0.0.1:5000/npews
def notpews():
    name = "npews" # here we declared a string variable in python file it,ll be parsed as var_name in the render_template html file
    return render_template('about.html', var_name = name) #check templates\about.html <h1>

app.run(debug=True)