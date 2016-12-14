import os
import glob
import time
import subprocess
from app import t, db, models
from threading import Thread
from datetime import datetime

def readTemp():
	p = subprocess.Popen( './projbbb', stdout=subprocess.PIPE, stdin=subprocess.PIPE )
	output = p.communicate( 'read temp\n' )[ 0 ]
	data = output.split(',')
	t.currentTemp = data[ 0 ]
	t.selectedTemp = data[ 1 ]
	t.selectedRange = data[ 2 ]

	if( data[ 3 ] == 'ON' ):
		t.power = True
	else:
		t.power = False

	brews = models.Brew.query.all()
	brewID = len(brews)
	b = models.Brew.query.get(brewID)
	ta = models.Temperature(temp_reading=t.currentTemp, timestamp=datetime.utcnow(), brewID=b)
	db.session.add(ta)
	db.session.commit()

def changeRange( newRange ):
	p = subprocess.Popen( './projbbb', stdout=subprocess.PIPE, stdin=subprocess.PIPE )
	command = 'set range ' + str( newRange ) + '\n'
	output = p.communicate( command )[ 0 ]

def changeDesired( newDesired ):
	p = subprocess.Popen( './projbbb', stdout=subprocess.PIPE, stdin=subprocess.PIPE )
	command = 'set desired ' + str( newDesired ) + '\n'
	output = p.communicate( command )[ 0 ]

def tempMain():
	while(True):
		readTemp()
		time.sleep(60)

th = Thread(target=tempMain)
th.start()
