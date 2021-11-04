from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/') #접속할 URL
def main():
	return render_template('index.html') #예제 템플릿

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)