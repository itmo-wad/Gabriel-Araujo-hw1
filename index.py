from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
  return redirect(url_for('profile'))

@app.route('/profile')
def profile():
  return render_template('profile.html')

if __name__ == '__main__':
	app.run(host='localhost', port=8080, debug=True)