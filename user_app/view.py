from user_app import userApp
from flask import request, render_template

@userApp.route('/')
def index():
    #user = request.args.get('user','Sourav')
    return render_template('index.html')
    #return "<h3>Working</h3>"