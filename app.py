import sqlite3
conn = sqlite3.connect('users.db')
c = conn.cursor()
print "Opened 'users.db' success"

from flask import Flask, render_template, url_for, request
app = Flask(__name__)

#route for homepage
@app.route('/')
def home():
	return render_template('home.html')

#route for login page
@app.route('/login/')
def login():
	return render_template('login.html')

@app.route('/adduser', methods = ['POST'])
def adduser():
   if request.method == 'POST':
	  try:
		 un = request.form['username']
		 print(un)
		 
		 with sqlite3.connect('users.db') as conn:
		 	c = conn.cursor()
			c.execute("INSERT INTO users VALUES (?)", (un))
			
			conn.commit()
			print("yup")
			msg = "Record successfully added"
	  except:
		 conn.rollback()
		 print("nope")
		 msg = "error in insert operation"
	  
	  finally:
		 return render_template("list.html",msg = msg)
		 conn.close()

#route for a public display of user.db
#for testing purposes of course :)
@app.route('/list/')
def list():
	conn = sqlite3.connect('users.db')
	c = conn.cursor()
	conn.row_factory = sqlite3.Row

	c.execute("select * from users")
   
	rows = c.fetchall(); 
	return render_template('list.html',rows = rows)

@app.route('/profile/')
def profile():
	return "This is my profile."

#what does this actually do?
if __name__ == '__main__':
	app.run()

#add threaded, os stuff