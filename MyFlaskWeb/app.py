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

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)