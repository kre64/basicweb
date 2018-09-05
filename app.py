from flask import Flask, render_template, url_for, request, redirect, session, escape
import sqlite3

app = Flask(__name__)
#Is this a bad key, look into good key generation?
app.secret_key = b'1_#4ieFR\n\xec]'

#Attempt connection to 'users.db'
conn = sqlite3.connect('users.db')
c = conn.cursor()
print ("Opened database 'users.db' success.")
conn.close()

#homepage
@app.route('/')
def home():
	if 'username' in session:
		session['logged_in']=True
		return render_template('mylist.html', username = session['username'])
	return render_template('home.html')

#login page
@app.route('/login/', methods=['GET'])
def login():
	if 'logged_in' in session:
		print("A user is still logged in")
		return redirect(url_for('home'))
	return render_template('login.html')

#logout route
@app.route('/logout/', methods=['GET'])
def logout():
    session.pop('username', None)
    session.pop('logged_in', None)
    return redirect(url_for('home'))

#post method for adding users
@app.route('/adduser/', methods=['GET', 'POST'])
def adduser():
	if 'logged_in' in session:
		print("A user is still logged in")
		return redirect(url_for('home'))
	if request.method == 'POST':
		conn = sqlite3.connect('users.db')
		c = conn.cursor()
		username = request.form['username']
		try:
			c.execute("INSERT INTO users (name) VALUES(?)",(username,))
			conn.commit()
			msg = "Record successfully added."
				
		except:
			conn.rollback()
			msg = "Error in insert operation, or user already exists."

		finally:
			print(msg)
			session['username'] = request.form['username']
			session['logged_in']=True
			return redirect(url_for('home'))
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
	if 'logged_in' not in session:
		print("A user is not logged in")
		return redirect(url_for('home'))
	return render_template('mylist.html')

#entry form for creating items
@app.route('/mylist/create', methods=['GET'])
def create():
	if 'logged_in' not in session:
		print("A user is still logged in")
		return redirect(url_for('home'))
	return render_template('create.html')

#post method for adding new items
@app.route('/additem', methods=['GET', 'POST'])
def additem():
	if 'logged_in' not in session:
		print("A user is not logged in")
		return redirect(url_for('home'))

	if request.method == 'POST':
		conn = sqlite3.connect('users.db')
		c = conn.cursor()
		current_user = session['username']
		new_item = request.form['createitem']
		status = 0
		try:
			c.execute("INSERT INTO lists (uname, item, isdone) VALUES (?, ?, ?)",(current_user, new_item, status))
			conn.commit()
			msg = "Item successfully added"

		except:
			conn.rollback()
			msg = "error in insert operation"

		finally:
			print(msg)
			return redirect(url_for('home'))
			conn.close()

# Get item list for user.
@app.route('/mylist/see', methods=['GET', 'POST'])
def see():
	if 'logged_in' not in session:
		print("A user is not logged in")
		return redirect(url_for('home'))
	if request.method == 'GET':
		current_user = session['username']
		conn = sqlite3.connect('users.db')
		conn.row_factory = sqlite3.Row
		c = conn.cursor()

		try:
			c.execute("SELECT * FROM lists WHERE uname LIKE (?)", (current_user,))
			rows = c.fetchall()
			msg = "Search for user list was successfull."
				
		except:
			msg = "Error in search."
			conn.rollback()

		finally:
			print(msg)
			return render_template('see.html', rows = rows)
			conn.close()

# Entry form for marking items as done.
@app.route('/mylist/markdone')
def markdone():
	if 'logged_in' not in session:
		print("A user is not logged in")
		return redirect(url_for('home'))
	return render_template('markdone.html')

# Check session username against db and update specified entry
@app.route('/markitem', methods=['GET', 'POST'])
def markitem():
	if 'logged_in' not in session:
		print("A user is not logged in")
		return redirect(url_for('home'))

	if request.method == 'POST':
		conn = sqlite3.connect('users.db')
		c = conn.cursor()
		current_user = session['username']
		target_item = request.form['markitem']
		try:
			c.execute("UPDATE lists SET isdone = 1 WHERE (uname) = (?) AND (item) = (?)", (current_user, target_item))
			conn.commit()
			msg = "Item successfully updated."
		except:
			conn.rollback()
			msg = "Error in update operation."

		finally:
			print(msg)
			return redirect(url_for('home'))
			conn.close()


#entry form for deleting items
@app.route('/mylist/deleteitems')
def deleteitems():
	if 'logged_in' not in session:
		print("A user is not logged in.")
		return redirect(url_for('home'))
	return render_template('delete.html')

#post method for deleting items
@app.route('/deleteitem', methods=['GET', 'POST'])
def deleteitem():
	if 'logged_in' not in session:
		print("A user is not logged in")
		return redirect(url_for('home'))

	if request.method == 'POST':
		conn = sqlite3.connect('users.db')
		c = conn.cursor()
		current_user = session['username']
		target_item = request.form['deleteitem']
		try:
			print("Attempting deletion of", target_item, "from list of user:", current_user)
			c.execute("DELETE FROM lists WHERE (uname) = (?) AND (item) = (?)", (current_user, target_item))
			conn.commit()
			msg = "Item successfully deleted"

		except:
			conn.rollback()
			msg = "error in delete operation"

		finally:
			print(msg)
			return redirect(url_for('home'))
			conn.close()

if __name__ == '__main__':
	app.run(host = '0.0.0.0')