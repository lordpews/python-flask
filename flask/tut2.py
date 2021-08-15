from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('about.html')

@app.route("/booty")
def booty():
    return render_template ('bootstrap.html')

@app.route("/pro")
def bad():
    return render_template('product.html')

app.run(debug=True)