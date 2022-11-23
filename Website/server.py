from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
   #  error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
           return redirect(url_for('index'))
            # error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('login'))
 

@app.route('/index')
def index():
   return render_template('index.html')

@app.route('/image')
def image():
   return render_template('image.html')

if __name__ == '__main__':
   app.run()