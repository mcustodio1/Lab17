#hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

#intance of flask
app= Flask(__name__)

bootstrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def hello():
    return 'Hello world For Lab 17!'

#hello_flask.py
@app.route('/mytemplate')
def t_test():
    return render_template('mytemplate.html')

#hello_flask.py
@app.route('/welcome')
def wc():
   s1 = 'Welcome to my page! '
   s2 = 'Have a nice day!'
   s3 = 'friends!'
   s4 = '213'
   return s1 + s2 + s3 + s4

# continute lab 17 

