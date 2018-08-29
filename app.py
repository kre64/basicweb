from flask import Flask, render_template, url_for
app = Flask(__name__)

#route for homepage
@app.route('/')
def home():
    return render_template('home.html')

#route for login page
@app.route('/login/')
def login():
    return render_template('login.html')

#what does this actually do?
if __name__ == '__main__':
	app.run()

#add threaded, os stuff