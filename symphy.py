#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
SYMPHY 2.0
'''

#global für Haptprogramm
DEBUG = True  #  True = Bildschirmausgabe
DEBUG2= True #  True = Abbruch bei Fehler


#std
import datetime
import time
import sys
import threading
from threading import Timer


# eigene module
import glb
from glb import sys_cfg,user_cfg,logger     #cfg parameter,logger
import bas
import cr

#globale Variablen aus modul glb
from glb import th						#thread variable
from glb import data					#daten variable

global th
global data


#Globale thread variablen neu
#
# 'id','name','para','exit'   -> für alle Start parameter

# id   = thread ID
# name = thread NameError
# para = thread Startparameter
# exit = true=exit thread
# xxx  = threat Variablen

  
	  
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
	
	msg='ini'
	logger.info(msg)

	#thread 0 tic  
	global thread_0
	id='0'
	name=th[id]['name']									#threat name
	mode=0												#Startparameter
	duration=0
	stic=0
	th[id]['exit']=False								#exit threat
	th[id]['para']=''				#startparameter
	thread_0 = my_threat(th[id])						#threat
	thread_0.setDaemon(True)   #thread endet mit dem Hauptprogramm
	thread_0.start()

	#thread 1 Light  
	global thread_1
	id='1'
	name=th[id]['name']									#threat name
	mode=0												#Startparameter
	duration=0
	stic=0
	th[id]['exit']=False								#exit threat
	th[id]['para']=name,mode,duration,stic				#startparameter
	thread_1 = my_threat(th[id])						#threat
	thread_1.setDaemon(True)   #thread endet mit dem Hauptprogramm
	thread_1.start()
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
	global th
	th['0']['exit']=True
	th['1']['exit']=True
	#th['2']['exit']=True

	msg='cleanup'
	logger.info(msg)
	return 	
	
	
"""
Threading
"""
class my_threat (threading.Thread):
	#
	#my Threading class
	#
	#Globale thread Variable th[th1]
	# ['id'] 
	# ['name']
	# ['data']
	#
	def __init__(self,th1):
		threading.Thread.__init__(self)
		#
		#
		self.id		= th1['id']			 #threat id
		self.name	= th1['name']		 #threat name
		self.para  =  th1['para']		 #threat parameter
		self.dt		= time.time()		 #threat start zeit eporch 
	def run(self):
		msg=('%s %10s ID[%s]' % ('Thread gestartet',self.name,self.id ))
		logger.info(msg)
		#
		if	 self.id==0:  cr.tic (self.para)	#tic modul cr
		elif self.id==1:  lightread (self.para)	#light
		#
		duration=round((time.time()-self.dt),2)
		duration2=bas.sec_to_txt2(duration) if duration > 60 else ""
		#
		msg=('%s %10s ID[%s] %ss %s' % ('Thread beendet	 ',self.name,self.id,duration,duration2))
		logger.info(msg)

def lightread(para):
	#
	#ID=1
	#
	global th
	name,mode,duration,stic =para
	#print "TOTAL DURATION: ","{:.1f}".format(time.time()-t1 )	
	#gesamtlaufzeit 
	#if th['2']['exit']: print "THREAD", name, "beendet"	 
	return

	
'''
Cron
'''
def cron(tx):
	#
	#Aufruf durch TIC Threat bei Änderung aus modul cr.py
	#
	
	if	tx=='s1':	cron_s1()
	elif tx=='s2':	cron_s2()
	elif tx=='s5':	cron_s5()
	elif tx=='s10':	cron_s10()
	elif tx=='s15':	cron_s15()
	elif tx=='s20':	cron_s20()
	elif tx=='s30':	cron_s30()
	#
	elif tx=='m1':	cron_m1()
	elif tx=='m2':	cron_m2()
	elif tx=='m5':	cron_m5()
	elif tx=='m10':	cron_m10()
	elif tx=='m15':	cron_m15()
	elif tx=='m20':	cron_m20()
	elif tx=='m30':	cron_m30()
	#
	elif tx=='h1':	cron_h1()
	elif tx=='h2':	cron_h2()
	elif tx=='h4':	cron_h4()
	elif tx=='h6':	cron_h12()	 #mittag und mitternacht
	#
	elif tx=='noon':	cron_noon()	 #12:00 Mittag
	elif tx=='midnight':cron_midnight()	 #00:00 Miternacht
	elif tx=='daily':	cron_daily()	 #täglich 04:00
	return
	

	
def cron_s1():
	logger.debug("TIC 1")
	return	
	
def cron_s2():
	logger.debug("TIC 2")
	return	

def cron_s5():
	logger.debug("TIC 5")
	return	
	
def cron_s10():
	logger.debug("TIC 10")
	return
	
def cron_s15():
	logger.debug("TIC 15")
	return	
	
def cron_s20():
	logger.debug("TIC 20")
	return	
	
def cron_s30():
	logger.debug("TIC 30")
	return	
	
def cron_m1():
	logger.info("TIC MIN")
	return 
	
def cron_m2():
	logger.debug("TIC MIN2")
	return

def cron_m5():
	logger.debug("TIC MIN5")
	return
	
def cron_m10():
	logger.debug("TIC MIN10")
	return
	
def cron_m15():
	logger.debug("TIC MIN15")
	return	
	
def cron_m0():
	logger.debug("TIC MIN20")
	return

def cron_m30():
	logger.debug("TIC MIN30")
	return

def cron_h1():
	logger.debug("TIC HOUR")
	return

def cron_h2():
	logger.debug("TIC HOUR2")
	return	
	
def cron_h4():
	logger.debug("TIC HOUR4")
	return	
	
def cron_h6():
	logger.debug("TIC HOUR6")
	return

def cron_h12():
	logger.debug("TIC HOUR 12")
	return	
	
def cron_noon():
	logger.debug("TIC Noon")
	return	
	
def cron_midnight():
	logger.debug("TIC MIDNIGHT")
	return
		
def cron_daily():
	logger.debug("TIC daily")
	return	
	

	
	
'''
Hauptprogramm
'''
def main(argv): 
	msg="-- SYMPHY2 START --"
	logger.info(msg)
	
	global data
	
	ini()	#initialisierung
		
	
	try:
		
		#raise NameError('HeyDu')
		

	
		'''
		Hauptschleife START
		'''
		while True:

			#print ('-')
			time.sleep(0.2)
			
			#raise NameError('HeyDu')
			#print ('-- main ---',data['dt']['asc'])

		'''
		Hauptschleife ENDE 
		'''
		return
		
		
		
	#FEHLER Hauptschleife
	except Exception:	
		if DEBUG2:
			raise			# Raise the error if DEBUG2=True
		msg='%s %s' %('Main Loop ',sys.exc_info()[1])
		logger.error(msg)
		
	finally:
		#cleanup
		clean()
		sys.exit
	return #from main

	
	
	
  
  

if __name__ == '__main__':	
	main(sys.argv[1:])
	sys.exit
	


















