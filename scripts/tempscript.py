#!/usr/bin/env python
import plotly.plotly as py
import time
from math import *
from plotly.graph_objs import *
import Adafruit_BBIO.ADC as adc
import datetime

adc.setup()

py.sign_in('michaelfbrown','vzrc271bcl')
#py.sign_in('alexanderallenbrown','mfqklqcwh8')
time.sleep(5)

trace2 = Scatter(
        x=[],
        y=[], 
        stream=dict(token='pb5s8ln1eh')
	#stream = dict(token='3dh5iql79h')
)


data = Data([trace2])
#fig = Figure(data=data,layout=layout)
#py.plot(fig)
py.plot(data)

s = py.Stream('pb5s8ln1eh')
#s = py.Stream('3dh5iql79h')
s.open()

starttime = time.time()

while True:
	t = time.time()-starttime
	val = adc.read("P9_40")
	volts = val*3
	temp = -40+volts*100 #10 mV/deg C, starting at -40 deg C
	tempF = 32+ temp*5.0/8.0
	x=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
	s.write(dict(x=x,y=tempF))
	time.sleep(.5)

s.close()

