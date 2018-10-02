#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CR
https://stackoverflow.com/questions/12435211/python-threading-timer-repeat-function-every-n-seconds
"""

#std
from threading import Timer
import time



#eigene  
import glb
from glb import sys_cfg,user_cfg,logger     # cfg parameter, logger
import bas
from symphy import cron

#globale Variablen aus modul glb
from glb import th						#thread variable
from glb import data					#daten variable

global th
global data

msg= 'modul %s  %s' %(bas.mod_name(),'ok')
logger.info(msg)


"""
TIC
"""
			
def gettime():
	#
	#Aktuele Zeit und Datum als Dictionary 
	#
	#out:  {'asc': asc,'epoch':epoch,'tp':tp}
	# 
	# ofs=(time.timezone*-1) + (time.localtime().tm_isdst)*3600 #offset in sekunden zu utc
	# true=Sommerziet tp.tm_isdst==1 							#sommerzeit
	# tp= time.localtime(epoch) 
	# tp= time.strptime(string,format)
	#
	#
	DT_FORMAT = sys_cfg['sys']['dt_format']			#Format Datum Zeit STD
	tp = time.localtime()               			# tupel
	asc = time.strftime(DT_FORMAT,tp)   			# ascii string  -> time.strptime(string,format) wandelt wieder zurück in tupel
	epoch=time.mktime(tp)							# epoch
	result = {'asc': asc,'epoch':epoch,'tp':tp}     
	return result

def tic(para):
	#
	#
	#
	global th
	global data
	#
	def tic0():
		#
		#0.5 Sekunden tic
		#
		global data
		#
		data['dt']=gettime()#systemzeit holen
		lt= data['dt']['tp']
		sec=lt.tm_sec
		min=lt.tm_min
		hour=lt.tm_hour
		#if sec % 1 == 0:  cron('s1')
		if sec % 2 == 0:  cron('s2')
		if sec % 5 == 0: 
			cron('s5')
			chk_light()		#licht modus prüfen zur vollen minute   TEST
		if sec % 10 == 0: cron('s10')
		if sec % 15 == 0: cron('s15')
		if sec % 20 == 0: cron('s20')
		if sec % 30 == 0: cron('s30')
		if sec == 0:
			#chk_light()		#licht modus prüfen zur vollen minute
			cron('m1')
			
			
			if min % 2 == 0: cron('m2')
			if min % 5 == 0: cron('m5')
			if min % 10 == 0: cron('m10')
			if min % 15 == 0: cron('m15')
			if min % 20 == 0: cron('m20')
			if min % 30 == 0: cron('m30')
			if min == 0:
				cron('h1')
				if hour % 2 == 0:  cron('h2')
				if hour % 4 == 0:  cron('h4')
				if hour % 6  == 0: cron('h6')
				if hour % 12  == 0:cron('h12')      #mittag und mitternacht
				if hour == 12 : cron('noon')        #mittag
				if hour == 0 : cron('midnight')     #miternacht
				if hour == 4: cron_('daily')        #täglich 04:00
		return
	#
	msg='tic timer start'
	logger.debug(msg)
	# Threat Schleife
	while not(th['0']['exit']):
		time.sleep(0.5)
		tic0()
	return

	
"""
INTERVAL TIMER
"""
	
def time_in_range(x, start, end):
	#
	#Prüft auf Zeit innerhalb Start Ende Intervall 
	#Rückgabe Zeit bis zum nächsten Wechsel
	#https://stackoverflow.com/questions/10747974/how-to-check-if-the-current-time-is-in-range-in-python
	#
	#in:
	#   start datetime.time		intevall Startzeit
	#   end   datetime.time		intervall Endzeit
	#   x     datetime.time 	zu prüfende Zeit
	#
	#out:
	#	res bool  				true wenn innerhalt des Intervalls
	#	d   datetime.time		Zeit bis zum nächsten wechsel
	#
	today = datetime.date.today()
	start = datetime.datetime.combine(today, start)
	end = datetime.datetime.combine(today, end)
	x = datetime.datetime.combine(today, x)
	end2=end 
	x2=x
	if end <= start:
		end += datetime.timedelta(1) # morgen
	if x <= start:
		x += datetime.timedelta(1)   # morgen
	res = start <= x <= end			 #intervallprüfung
	#restlaufzeit
	if res: 							#innerhalt des intervalls
		d=end-x
	else:								#außerhalb des intervalls
		if x2 >= start:					
			start += datetime.timedelta(1) # tomorrow!
			d=start-x2
		else:
			d=start-x2
	return res,d 

	
	

def chk_light():
	logger.info('checking Lighmode')
	
	param = user_cfg['light']		#User Parameter Licht
	SysTime=data['dt']['tp']		#systemzeit tupel
	 
	return 
	 	 
	#Sonnenaufgang - sun_u
	c1 = param['sun']['up_start']                  #startzeit [hh:mm]
	c2 = param['sun']['up_end']                    #endzeit [hh:mm]  
	sun_u,x3 = time_in_range(SysTime,c1,c2)         #Intervall prüfen
	
	
	x4=int(x3/60)                                  #zeit bis wechsel in vollen minuten
	x3tx=bas.min_to_txt(x4)
	
	
	msg= ('%-18s %-5s %-5s %-5s %-5s %-5s' %   ( 'Sonnenaufgang ',c1,c2,sun_u,x4,x3tx)) 
	if sun_u:
		gl_toggle=x4                                #zeit bis wechsel in minuten
		gl_start=c1                                 #Startzeit [hh:mm] 
		gl_end=c2                                   #Endzeit [hh:mm]
	 
	logger.debug(msg)
	 
	 
	 
	 

	 
	return
	
	

