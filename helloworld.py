from flask import Flask, render_template, flash, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired


#Create flask instance
app = Flask(__name__)

#Create bootstrap instance
bootstrap = Bootstrap(app)

#Create moment instance
moment = Moment(app)

app.config['SECRET_KEY'] = 'string'

def contains_utoronto(form, field):
	if 'utoronto' not in field.data:
		raise ValidationError('Email must contain "utoronto"')

def contains_and(form, field):
	if '@' not in field.data:
		raise ValidationError(f"Please include '@' in the email address. '{field.data}' is missing an '@'")


class NameForm(FlaskForm):
	name = StringField('What is your name?', validators=[DataRequired()])
	email = StringField('What is your UofT Email address?', validators=[DataRequired(), contains_and, contains_utoronto])
	submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()

	if form.validate_on_submit():

		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('Looks like you have changed your name!')
		session['name'] = form.name.data
		session['email'] = form.email.data
		return redirect(url_for('index'))


	return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'))

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)



if __name__ == '__main__':
	app.run()
