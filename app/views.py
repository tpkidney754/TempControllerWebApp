from flask import render_template, redirect, url_for, flash
from app import app
from .forms import ChangeSettingsForm, NewBrewForm, BrewHistoryForm
from app import t, db, models
from datetime import datetime
import readTemp
from createPlot import createPlot

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	readTemp.readTemp()
	return render_template('index.html',
							currentTemp=t.currentTemp,
							selectedTemp=t.selectedTemp,
							selectedRange=t.selectedRange,
							status=t.power)

@app.route('/changeSettings', methods=['GET', 'POST'])
def changeSettings():
	form = ChangeSettingsForm()
	if form.validate_on_submit():
		readTemp.changeDesired( int(form.desiredTemp.data) )
		readTemp.changeRange( int(form.desiredRange.data) )
		return redirect('/index')
	else:
		print "Failed submit"

	return render_template('changeSettings.html',
							title="Change Settings",
							currentTemp=t.currentTemp,
							selectedTemp=t.selectedTemp,
							selectedRange=t.selectedRange,
							status=t.power,
							form=form
							)

@app.route('/brews', methods=['GET', 'POST'])
def brews():
	global brewID
	global plotFileName
	newBrewForm = NewBrewForm()
	brewHistoryForm = BrewHistoryForm()
	if newBrewForm.validate_on_submit():
		newBrew = models.Brew(name=newBrewForm.newBrew.data, start_date=datetime.utcnow())
		db.session.add(newBrew)
		db.session.commit()
		flash('Starting new fermentation for %s beginning on %s' % (newBrew.name, newBrew.start_date))
		return redirect(url_for('index'))

	if brewHistoryForm.validate_on_submit():
		brewIDnum = brewHistoryForm.brewName.data;
		plotFileName = createPlot(brewIDnum)
		return redirect(url_for('fig'))

	else:
		flash('Validation failed for brew history')

	return render_template('brews.html',
							newBrewForm=newBrewForm,
							brewHistoryForm=brewHistoryForm)

@app.route('/fig')
def fig():
	global plotFileName
	return render_template('fig.html',
							plotFileName=plotFileName)

@app.errorhandler(404)
def notFoundError(error):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internel_error(error):
	db.session.rollback()
	return render_template('500.html'), 500
