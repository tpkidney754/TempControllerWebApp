from flask_wtf import FlaskForm as Form
from wtforms import StringField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired
from app import t, db, models
from sqlalchemy import desc

class ChangeSettingsForm(Form):
	desiredTemp = StringField('desiredTemp', default=t.selectedTemp, validators=[DataRequired()])
	desiredRange = StringField('desiredRange', default=t.selectedRange, validators=[DataRequired()])

class NewBrewForm(Form):
	newBrew = StringField('newBrewName', validators=[DataRequired()])

class BrewHistoryForm(Form):
	brews = models.Brew.query.order_by(desc('start_date')).all()
	#brews = models.Brew.query.all()
	choices = []
	for bb in brews:
		field = bb.name + ' started on ' + str(bb.start_date)
		choices.append([bb.id, field])

	brewName = SelectField('brewName', choices=choices, coerce=int)
