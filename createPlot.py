import matplotlib.pyplot as plt
from numpy import *
from app import db, models
import os
from datetime import datetime

def createPlot(brewIDnum):
	b = models.Brew.query.get(brewIDnum)
	plotTitle = '%s that was started on %s' % (b.name, b.start_date)
		
	tempData = b.temp_data.all()
	temps = []
	dates = []
	x = []
	i = 1

	for td in tempData:
		temps.append(td.temp_reading)
		dates.append(td.timestamp)
		x.append(i)
		i += 1
	
	plt.clf()
	plt.plot(x,temps)
	
	'''
	labels = []
	for dt in dates:
		labels.append(dt.isoformat())

	plt.xticks(x, labels, rotation='vertical')
	plt.margins(0.2)
	plt.subplots_adjust(bottom=0.25)
	'''
	plt.ylabel('Temperature in F')
	plt.title(plotTitle)
	d = datetime.utcnow()
	dir = os.path.dirname(os.path.realpath(__file__))
	plotFileNameFull = dir + '/app/static/img/Plots/' + b.name + b.start_date.isoformat() + '/plot_' + d.isoformat() +'.png'
	dir = os.path.dirname(plotFileNameFull)
	print dir
	try:
		os.stat(dir)
	except:
		os.mkdir(dir)
	
	plotFileName = '/static/img/Plots/' + b.name + b.start_date.isoformat() + '/plot_' + d.isoformat() +'.png'
	plt.savefig(plotFileNameFull)

	return plotFileName