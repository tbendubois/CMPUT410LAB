from flask import *
import os
import sqlite3

app = Flask(__name__)
app.debug = True
app.config["SERVER_NAME"] = "127.0.0.1:8888"


dbFile = "tasks.db"
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

def add_task(c, p, d):
	q = "INSERT INTO task (category, priority, description) VALUES (?, ?, ?)"
	query_db(q, (c, p, d))
	get_conn().commit()
	
def get_tasks():
	t = []
	cur = get_conn().cursor()
	cur.execute("select category, priority, description from task")	
	for row in cur:
		t.append({"category":row[0],
		         "priority":row[1],
		         "description":row[2]})
	cur.close()
	return t

@app.route('/')
def hello_world():
	return "Hello, world!"

@app.route("/task", methods=["GET", "POST"])
def task():
	#get
	resp = ""
	resp = resp + """
	<form action = "" method = post>
	  <p>Category<input type=text name=category></p><br/>
	  <p>Priority<input type=number name=priority></p><br/>
	  <p>Description<input type=text name=description></p><br/>
	  <p><input type=submit value=Add></p>
	</form>
	
	<table border="1" cellpadding="3">
	  <tbody>
	    <tr>
	      <th>Category</th>
	      <th>Priority</th>
	      <th>Description</th>
	    </tr>
	  
	"""
	tasks = get_tasks()
	for task in tasks:
		resp = resp + "<tr><td>%s</td>" %(task["category"])
		resp = resp + "<td>%s</td>" %(task["priority"])
		resp = resp + "<td>%s</td></tr>" %(task["description"])
		
	if request.method == "GET":
		return resp
		
	if request.method == "POST":
		category = request.form["category"]
		pri = request.form["priority"]
		desc = request.form["description"]
		
		
		add_task(category, pri, desc)
		#tasks.append({"category":category,
		 #              "priority":pri,
		  #             "description":desc})
		
		return redirect(url_for("task"))
	
	
if __name__ == "__main__":
	app.run()