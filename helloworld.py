from flask import Flask

#Create flask instance
app = Flask(__name__)

@app.route('/')
def hello_world():
	return '<H1>Hello world!</H1>'

if __name__ == '__main__':
	app.run()
