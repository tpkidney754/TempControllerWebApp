from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Temp import Temp
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD

t = Temp()
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


if not app.debug:
	import logging
	from logging.handlers import SMTPHandler
	from logging.handlers import RotatingFileHandler
	file_handler = RotatingFileHandler('tmp/tempcontroller.log', 'a', 1*1024*1024, 10)
	file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(messages)s'+
							'[in %(pathname)s:%lineno)d]'))
	app.logger.setLevel(logging.INFO)
	file_handler.setLevel(logging.INFO)
	app.logger.addHandler(file_handler)
	#app.logger.info('Temp Controller startup')
	credentials = None
	if MAIL_USERNAME or MAIL_PASSWORD:
		credentials = (MAIL_USERNAME, MAIL_PASSWORD)
	mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@' + MAIL_SERVER, ADMINS,
								 'Temp Controller failure', credentials)
	mail_handler.setLevel(logging.ERROR)
	app.logger.addHandler(mail_handler)

from app import views, models