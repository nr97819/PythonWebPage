from flask import Flask, Blueprint, json, request, render_template, make_response, jsonify, redirect, url_for
from flask_login import login_user, current_user, logout_user
from flask_login.utils import login_required
from server_controller.user_setting import User

import datetime

main_obj = Blueprint('service', __name__)

@main_obj.route('/signin', methods=['GET','POST'])
def signin():
    if request.method =='GET':
        # print('username : ', request.form['username'])
        # print('password : ', request.form['password'])
        if current_user.is_authenticated:
            # session에서 username 추출 및 반환
            return render_template('signin.html', username=current_user.username)
        else:
            return render_template('signin.html')

    elif request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        print('username2 : ', username)
        print('password : ', password)
        # print('direct_flag : ', request.form['direct_flag'])

        # user = User.find(request.form['username'], request.form['password'])
        user = User.examine(username, password)
        
        if(user == None):
            return render_template('signin.html', warning='등록되지 않은 계정입니다')
        # elif(user == 'test'):
        #     return render_template('signin.html', warning='존재하지 않는 계정입니다')
        else:
            login_user(user, remember=True, duration=datetime.timedelta(minutes=1))
            print('?')
            
            # direct_flag=request.form['direct_flag']
            # print(111)
            # if(direct_flag):
            #     logout_user()
        
        # return redirect(url_for('service.signin'))
        return redirect('/service/signin')

@main_obj.route('/logout', methods=['GET','POST'])
def logout():
    logout_user()
    return redirect('/service/signin')

@main_obj.route('/register', methods=['GET','POST'])
def register():
    if request.method =='GET':
    	return render_template('register.html')

    elif request.method == 'POST':
        print('username : ', request.form['username'])
        print('password : ', request.form['password'])
        
        User.create(request.form['username'], request.form['password'])
        
        return redirect('/service/signin')
        # return redirect(url_for('service.signin'))
        # return make_response(jsonify(success=True), 200)
    
    # return render_template('signin.html')
    
@main_obj.route('/product')
def product():
    return render_template('pricing.html')