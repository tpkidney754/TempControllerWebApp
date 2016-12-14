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

'''
GPIO.setmode(GPIO.BCM)
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
relayPin = 23
base_dir = '/sys/bus/w1/devices/'
deviceFolder = glob.glob(base_dir + '28*')[0]
device_file = deviceFolder + '/w1_slave'
GPIO.setup(relayPin, GPIO.OUT, initial = 1)

def read_temp_raw():
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close
	return lines

def read_temp():
	lines = read_temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = read_temp_raw()
	equals_pos = lines[1].find('t=')
	if(equals_pos != 1):
		tempString = lines[1][equals_pos+2:]
		tempC = float(tempString)/1000.0
		tempF = tempC*9.0/5.0 + 32.0
		return float("%.2f" % tempF)

def turnOn(pin):
	GPIO.output(relayPin, 0)
	return

def turnOff(pin):
	GPIO.output(relayPin, 1)
	return

def refreshTemp():
	t.currentTemp = read_temp()

	if(t.power == False):
		if(t.currentTemp > t.selectedTemp + t.selectedRange):
			t.power = True
			turnOn(relayPin)
	else:
		if(t.currentTemp <= t.selectedTemp):
			t.power = False
			turnOff(relayPin)

	brews = models.Brew.query.all()
	brewID = len(brews)
	b = models.Brew.query.get(brewID)
	ta = models.Temperature(temp_reading=t.currentTemp, timestamp=datetime.utcnow(), brewID=b)
	db.session.add(ta)
	db.session.commit()

def tempMain():
	while(True):
		refreshTemp()
		time.sleep(60)

th = Thread(target=tempMain)
th.start()
'''
