from flask import Flask, jsonify, request, render_template, make_response, session, redirect, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from server_view import view
from server_controller.user_setting import User
import os
import random

# https 만을 지원하는 기능을 http 에서 테스트할 때 필요한 설정
# os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static')
# CORS(app)
# app.secret_key = '1trillionKey'
app.secret_key = str(int(random.random()*10000000000))
print(app.secret_key)

app.register_blueprint(view.main_obj, url_prefix='/service')
login_manager = LoginManager()
login_manager.init_app(app)
# session을 보다 복잡하게 만들어준다.
login_manager.session_protection = 'strong'

# 테스트중
@app.route('/') # 접속할 URL
def home():
    return redirect('/service/signin')

# 테스트중
@app.route('/register_1', methods=['GET','POST']) # 접속할 URL
def register_level_1():
	return render_template('register_1.html')

@app.route('/register_2', methods=['GET','POST']) # 접속할 URL
def register_level_2():
    return render_template('register_2.html')

@app.route('/register_3', methods=['GET','POST']) # 접속할 URL
def register_level_3():
    print('level = 3')
    print('username : ', request.form['username'])
    print('password : ', request.form['password'])
    username=request.form['username']
    password=request.form['password']
    return render_template('register_3.html', username=username, password=password)

@app.route('/register_4', methods=['GET','POST']) # 접속할 URL
def register_level_4():
    print('level = 4')
    print('username : ', request.form['username'])
    print('password : ', request.form['password'])
    username=request.form['username']
    password=request.form['password']
    
    User.create(request.form['username'], request.form['password'])
        
    return render_template('register_4.html', username=username, password=password)

@app.route('/complete', methods=['GET','POST']) # 접속할 URL
def register_complete():
    print('username : ', request.form['username'])
    print('password : ', request.form['password'])
    username=request.form['username']
    password=request.form['password']
    return render_template('signin.html', username=username, password=password, direct_flag=True)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)

# @app.before_request
# def app_before_request():
#     if 'client_id' not in session:
#         session['client_id'] = request.environ.get(
#             'HTTP_X_REAL_IP', request.remote_addr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
