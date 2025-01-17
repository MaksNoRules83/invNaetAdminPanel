from flask import Flask
from flask import render_template, url_for
import sqlite3

app = Flask(__name__)

db = sqlite3.connect("invNAET.db")
cursor = db.cursor()

@app.route("/")
def index():
    return render_template("login.html")

@app.route('/adminpanel/users')
def adminpanel():
    return render_template("users.html")

@app.route('/adminpanel/inventories')
def inventories():
    return render_template('inventories.html')

@app.route('/adminpanel/cabinets')
def cabinets():
    return render_template('cabinets.html')

@app.route('/adminpanel/profile')
def profile():
    return render_template('profile.html')

@app.route('/adminpanel/jobs')
def jobs():
    return render_template('jobs.html')


if __name__ == "__main__":
    app.run()
