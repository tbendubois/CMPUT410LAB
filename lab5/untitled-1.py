from flask import *
import os
import sqlite3

app = Flask(__name__)
app.debug = True
app.config["SERVER_NAME"] = "127.0.0.1:8888"

def get_conn():
	global conn
	if conn is None:
		conn = sqlite3.connect(dbFile)
		conn.row_factory = sqlite3.Row
	return conn
		
@app.teardown_appcontext
def close_connection(exception):
	global conn
	if conn is not None:
		conn.close()
		conn = None

def query_db(query, args=()):
	cur = get_conn().cursor()
	cur.execute(query, args)
	r = cur.fetchall()
	cur.close()
	return (r[0] if r else None)


@app.route('/')
def welcome():
	return "Hello, world!"

@app.route("/task", methods=["GET", "POST"])
def task():
	return render_template('show_entries.html',
	                       tasks=query_db("select * from task"))
	
@app.route("/login",methods=["GET","POST"])
def login():
	return render_template('login.html', error=None)

if __name__ == "__main__":
	app.run()