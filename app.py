from flask import Flask, render_template, url_for, request, redirect, session, escape
import sqlite3

app = Flask(__name__)
app.secret_key = b'1_#4ieFR\n\xec]' #bad key

#create_connection to 'users.db'
conn = sqlite3.connect('users.db')
c = conn.cursor()
print ("Opened 'users.db' success")
conn.close()

#homepage
@app.route('/')
def home():
	if 'username' in session:
		#return 'Logged in as %s' % escape(session['username'])
		return render_template('mylist.html', username = session['username'])
	return render_template('home.html')

#login page
@app.route('/login/')
def login():
	return render_template('login.html')

#logout route
@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

#post method for adding users
@app.route('/adduser/', methods=['GET', 'POST'])
def adduser():
	if request.method == 'POST':
		conn = sqlite3.connect('users.db')
		c = conn.cursor()
		username = request.form['username']

		#check if username already exists
		try:
			#username = request.form['username']
			c.execute("INSERT INTO users (name) VALUES(?)",(username,))
			conn.commit()
			msg = "Record successfully added"
				
		except:
			#There was an error
			conn.rollback()
			msg = "error in insert operation"

		finally:
			print(msg)
			#resp =  make_response(render_template('home.html'))
			#resp.set_cookie('username', username)
			#return resp
			session['username'] = request.form['username']
			return render_template('home.html')
			conn.close()

#public display of user.db
#for testing purposes of course :)
@app.route('/list/', methods=['GET', 'POST'])
def list():
	conn = sqlite3.connect('users.db')
	conn.row_factory = sqlite3.Row
	c = conn.cursor()

	c.execute("SELECT * FROM users")
	rows = c.fetchall(); 

	return render_template('list.html', rows = rows)
	conn.close()

#user profile page
@app.route('/mylist/', methods=['GET', 'POST'])
def mylist():
	username = request.cookies.get('username')
	return render_template('mylist.html')

#what does this actually do?
if __name__ == '__main__':
	app.run()

#add threaded, os stuff