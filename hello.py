from flask import Flask , session, redirect, url_for, escape, request ,render_template, send_from_directory
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return send_from_directory('static','index.html')

# @app.route('/static')
# def static(path):
#     return send_from_directory('static', path)

@app.route('/login')
def login():
    app.logger.debug('A value for debugging')