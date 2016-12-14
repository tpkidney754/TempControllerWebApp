from flask_wtf import Form
from wtforms import StringField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired
from app import t, db, models

class ChangeSettingsForm(Form):
	desiredTemp = StringField('desiredTemp', default=t.selectedTemp, validators=[DataRequired()])
	desiredRange = StringField('desiredRange', default=t.selectedRange, validators=[DataRequired()])

class NewBrewForm(Form):
	newBrew = StringField('newBrewName', validators=[DataRequired()])

class BrewHistoryForm(Form):
	brews = models.Brew.query.order_by('start_date').all()
	#brews = models.Brew.query.all()
	choices = []
	for bb in brews:
		field = bb.name + ' started on ' + str(bb.start_date)
		choices.append([bb.id, field])

	brewName = SelectField('brewName', choices=choices, coerce=int)
