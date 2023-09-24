from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
#Create flask instance
app = Flask(__name__)

#Create bootstrap instance
bootstrap = Bootstrap(app)

#Create moment instance
moment = Moment(app)

@app.route('/')
def hello_world():
	return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)



if __name__ == '__main__':
	app.run()
