#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
SYMPHY 2.0
'''

#global für Haptprogramm
DEBUG = True  #  True = Bildschirmausgabe
DEBUG2= False #  True = Abbruch bei Fehler


#std
import datetime
import time
import sys

import threading	#https://docs.python.org/2/library/threading.html#timer-objects


# eigene module
import glb
from glb import sys_cfg,user_cfg,logger     #cfg parameter,logger
import bas


tic=0


'''
Initialisierung
Cleanup
'''

def ini():
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
	print ('INIT')
	
	#cron job starten	
	#threading.Timer(5.0, cron_tic).start() # 5 Sekunden cron starten
	#print ('5 Sekunden cron gestartet')
	cron_tic()
	
	return 

	
def clean():
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
	
	print ('CLEANUP')
	return 	

'''
Timer
Cron
tic
'''
	
def time_in_range(start, end, x):
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
	
def cron_tic():

	anz=threading.enumerate()
	print ("Threads: ",anz)

	threading.Timer(1.0, cron_tic).start() # 5 Sekunden cron neu starten
	
	
	
	
	lt=time.localtime()
	sec=lt.tm_sec
	min=lt.tm_min
	hour=lt.tm_hour
	print(hour,min,sec)
	if sec % 2 == 0: cron_2()
	if sec % 5 == 0: cron_5()
	if sec % 10 == 0: cron_10()
	if sec % 15 == 0: cron_15()
	if sec % 20 == 0: cron_20()
	if sec % 30 == 0: cron_30()
	if sec == 0:
		cron_min()
		if min % 2 == 0: cron_min2()
		if min % 5 == 0: cron_min5()
		if min % 10 == 0: cron_min10()
		if min % 15 == 0: cron_min15()
		if min % 20 == 0: cron_min20()
		if min % 30 == 0: cron_min30()
		if min == 0:
			cron_hour()
			if hour % 2 == 0: cron_hour2()
			if hour % 4 == 0: cron_hour4()
			if hour % 6  == 0: cron_hour6()
			if hour % 12  == 0: cron_hour12()   #mittag und mitternacht
			if hour == 12 : cron_noon()         #mittag
			if hour == 0 : cron_midnight()      #miternacht
			if hour == 4: cron_daily()          #täglich 04:00
	return
	
	
	
def cron_2():
	print("TIC 2")
	logger.debug("TIC 2")
	return	

def cron_5():
	print("TIC 5")
	logger.debug("TIC 5")
	return	
	
def cron_10():
	print("TIC 10")
	logger.debug("TIC 10")
	return
	
def cron_15():
	print("TIC 15")
	logger.debug("TIC 15")
	return	
	
def cron_20():
	print("TIC 20")
	logger.debug("TIC 20")
	return	
	
	
def cron_30():
	print("TIC 30")
	logger.debug("TIC 30")
	return	
	
def cron_min():
	print("TIC MIN")
	logger.debug("TIC MIN")
	return

def cron_min2():
	print("TIC MIN 2")
	logger.debug("TIC MIN2")
	return

def cron_min5():
	print("TIC MIN 5")
	logger.debug("TIC MIN5")
	return
	
	
def cron_min10():
	print("TIC MIN 10")
	logger.debug("TIC MIN10")
	return
	
def cron_min15():
	print("TIC MIN 15")
	logger.debug("TIC MIN15")
	return	
	
def cron_min20():
	print("TIC MIN 20")
	logger.debug("TIC MIN20")
	return

def cron_min30():
	print("TIC MIN 30")
	logger.debug("TIC MIN30")
	return

def cron_hour():
	print("TIC HOUR")
	logger.debug("TIC HOUR")
	return

def cron_hour2():
	print("TIC HOUR 2")
	logger.debug("TIC HOUR2")
	return	
	
def cron_hour4():
	print("TIC HOUR 4")
	logger.debug("TIC HOUR4")
	return	
	
def cron_hour6():
	print("TIC HOUR 6")
	logger.debug("TIC HOUR6")
	return

def cron_hour12():
	print("TIC HOUR 12")
	logger.debug("TIC HOUR 12")
	return	
	
def cron_noon():
	print("TIC noon")
	logger.debug("TIC Noon")
	return	
	
def cron_midnight():
	print("TIC midnight")
	logger.debug("TIC MIDNIGHT")
	return

		
def cron_daily():
	print("TIC daily")
	logger.debug("TIC daily")
	return	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
'''
Hauptprogramm
'''
def main(argv): 


	try:
		
		#raise NameError('HeyDu')
		
		#initialisierung
		ini()
	
		'''
		Hauptschleife START
		'''
		while True:

			#print ('-')
			time.sleep(0.05)
			
			#raise NameError('HeyDu')

		'''
		Hauptschleife ENDE 
		'''
		return
		
		
		
	#FEHLER Hauptschleife
	except Exception:	
		if DEBUG2:
			raise			# Raise the error if DEBUG2=True
		print ('%s %s' %('Main Loop ',sys.exc_info()[1]))
		
		#msg='%s %s' %('Main Loop ',sys.exc_info()[1])
		#bas.log("error",msg)
		
	finally:
		#cleanup
		clean()
		sys.exit
	return #from main

	
	
	
  
  

if __name__ == '__main__':	
	main(sys.argv[1:])
	sys.exit
	


















