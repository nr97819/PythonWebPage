from re import U
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/') #접속할 URL
def main():
	return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
	if request.method =='GET':
		return render_template('register.html')
		
	elif request.method =='POST':
		# id=request.form.get('inputId')
		# pw=request.form.get('inputId')
		
		inputId=request.args.get('inputId')
		inputPw=request.args.get('inputPw')
		str = '%s' % inputId
		str += '%s' % inputPw
		
		return render_template('index.html', str=str)

@app.route('/agreement', methods=['GET','POST']) # 개인 정보 동의 페이지
def agree():
	if request.method =='GET':
		return render_template('agreement.html')
		
	elif request.method =='POST':
		return render_template('index.html')

@app.route('/uploading', methods=['GET','POST']) # 진단서 업로드 페이지
def upload():
	if request.method =='GET':
		return render_template('uploading.html')
		
	elif request.method =='POST':
		return render_template('index.html')

@app.route('/products', methods=['GET','POST']) # 상품 목록 페이지
def product():
	if request.method =='GET':
		return render_template('products.html')
		
	elif request.method =='POST':
		return render_template('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)