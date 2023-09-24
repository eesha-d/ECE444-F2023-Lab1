from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


#Create flask instance
app = Flask(__name__)

#Create bootstrap instance
bootstrap = Bootstrap(app)

#Create moment instance
moment = Moment(app)

app.config['SECRET_KEY'] = 'string'

class NameForm(FlaskForm):
	name = StringField('What is your name?', validators=[DataRequired()])
	submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	name=None
	form = NameForm()

	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('index.html', current_time=datetime.utcnow(), form=form, name=name)

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)



if __name__ == '__main__':
	app.run()
