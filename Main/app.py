from flask import Flask, render_template, g, request, redirect, url_for
import sqlite3
import os

#test
DATABASE = 'database.db'

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    db = get_db()
    shoes = db.execute('SELECT * FROM shoes').fetchall()
    return render_template('home.html', shoes=shoes)


@app.route("/shoes")
def shoes():
    db = get_db()
    shoes = db.execute('SELECT * FROM shoes').fetchall()
    return render_template('shoes.html', shoes=shoes)

if __name__ == "__main__":
    app.run(debug=True)