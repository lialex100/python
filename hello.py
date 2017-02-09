from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! 45623'
    
@app.route('/projects/')
def projects():
    return 'The project pageasdasasdeasssd'

@app.route('/about')
def about():
    return 'The about page'
