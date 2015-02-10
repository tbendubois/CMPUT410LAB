from flask import *
import os
import sqlite3
from random import *

app = Flask(__name__)
app.debug = True
app.config["SERVER_NAME"] = "127.0.0.1:8888"
app.config["USERNAME"] = "admin"
app.config["PASSWORD"] = "admin"
app.secret_key = "dogBark!"

max_int = 1000000000000000

dbFile = "todolist.db"

conn = None

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

def add_task(i, c, p, d):
	q = "INSERT INTO task VALUES (?, ?, ?, ?)"
	query_db(q, (i, c, p, d))
	get_conn().commit()
	
def get_tasks():
	t = []
	cur = get_conn().cursor()
	cur.execute("select * from task")	
	for row in cur:
		t.append({"ident":row[0],
		        "category":row[1],
		         "priority":row[2],
		         "description":row[3]})
	cur.close()
	return t

def removetask(ident):
	q = "DELETE FROM task WHERE id=?"
	query_db(q, (int(ident)))
	get_conn().commit()

@app.route('/')
def hello_world():
	return redirect(url_for("task"))

@app.route("/task", methods=["GET", "POST"])
def task():
	if request.method == "POST":
		if not session.get("logged_in"):
			abort(401)
		else:
			ident = randint(1, max_int)
			c = request.form["category"]
			p = request.form["priority"]
			d = request.form["description"]
			add_task(ident,c,p,d)
			flash("Add task was successful.")
			return redirect(url_for("task"))
	else:
		return render_template('show_entries.html',
	                       tasks=get_tasks())
	
@app.route("/login",methods=["GET","POST"])
def login():
	error = None
	if request.method == "POST":
		if (request.form["username"] != app.config["USERNAME"]) or\
		   (request.form["password"] != app.config["PASSWORD"]):
			error = "Invalid Username or Password"
			flash(error)
		else:
			session["logged_in"] = True
			flash("You are logged in")
			return redirect(url_for('task'))
		
	return render_template('login.html', error=error)

@app.route("/logout",methods=["GET","POST"])
def logout():
	session.pop('logged_in', None)
	flash("you are logged out")
	return redirect(url_for("task"))

@app.route("/delete",methods=["GET","POST"])
def delete():
	if not session.get("logged_in"):
		abort(401)
	removetask(request.form["ident"])
	
if __name__ == "__main__":
	app.run()
