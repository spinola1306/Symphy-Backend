# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
- globale Konstanten und Variablen 
- ini file und log file 
- Allgemeine Funktionssammlung
"""
  
#std 
import logging
import logging.handlers 

#extern
from configobj import ConfigObj           # ini dateien http://www.voidspace.org.uk/python/configobj.html#write


'''
Konstanten
'''	
#Licht Modus
# 	  
LIGHT_ARR=['Aus','Sonnenaufgang','Tag','Sonnenuntergang','Mondaufgang','Mondlicht','Monduntergang','Sternaufgang','Sternlicht','Sternenuntergang','Restlicht-Mond','Restlicht-Sterne']   	  
	  
	
'''
Variablen Untertypen
'''	
#System Zeit
# 
dt =	{
		'asc':'',
		'epoch':0,
		'struct':'',
		} 
	
	
'''
globale Variablen
'''	
	
#daten
#   
data =	{
		'dt':           dt, 					#system zeit
		}
	

#thread Variable th[th1]
# ['id'] 
# ['name']
# ['data']
#
th =	{
		'0': {'id':0,'name':'tic'    ,'para':None, 'exit':False},     #hauptprogramm 
		'1': {'id':1,'name':'LICHT'   ,'para':None, 'exit':False, 'name_arr':['LICHT NULL','LICHT SA','LICHT SU','LICHT MA','LICHT MU','LICHT SA','LICHT SU']},    # Thread2 Licht 
 		}


  
  
	  
	  
'''
Konfigurationsdateien
'''
 
def parse_cfg(name):
	#
	#Globale Initialisierung der ini datei 
	#lesen und schreiben
	#
	#http://www.voidspace.org.uk/python/configobj.html#write
	#
	#pfad für ini datei holen aus sys0.cfg
	cfg=ConfigObj('sys0.cfg')
	path=cfg['sys']['cfgpath']
	f_name='%s/%s' % (path,name)
	config=ConfigObj(f_name)
	return config
  
'''
Logging
'''
 
def parse_logger():
	#
	#logfile
	#
	#https://docs.python.org/2/howto/logging.html 
	#https://docs.python.org/2/library/logging.handlers.html
	#
	#konfiguration durch cfg file
	sec1 = sys_cfg['log']    
	loglevel_stderr =sec1['loglevel_stderr'].upper()
	loglevel_file   =sec1['loglevel_file'].upper()
	log_path=sec1['logpathname']
	#basis												   
	logger=logging.getLogger('basis')
	logger.setLevel(logging.DEBUG)		
	#formatierung template
	formatter = logging.Formatter(
				'%(asctime)s %(levelname)-8s %(module)-6s %(threadName)-12s %(lineno)-4s : %(message)s',
				datefmt='%d.%m.%Y %H:%M:%S')
	#rotating file handler
	rf = logging.handlers.RotatingFileHandler(log_path,	#handler
													   maxBytes=sec1.as_int('maxbytes'),
													   backupCount=sec1.as_int('backupcount'),
													   encoding='utf-8',
													   mode='a',
													)
	rf.setFormatter(formatter)							#Format
	loglevel=loglevel_file								#Log Level
	if  loglevel == 'DEBUG':
		lev=logging.DEBUG
	elif loglevel == 'INFO':
		lev=logging.INFO
	elif loglevel == 'WARNING':
		lev=logging.WARNING 
	elif loglevel == 'ERROR':
		lev=logging.ERROR 
	elif loglevel == 'CRITICAL':
		lev=logging.CRITICAL
	else: lev=100 #logging ausgeschaltet

	rf.setLevel(lev)							
	logging.getLogger('basis').addHandler(rf)				#add the handlers to the root logger

	
	# sys.stderr
	console = logging.StreamHandler()					#handler
	console.setFormatter(formatter)						#Formatierung
	loglevel=loglevel_stderr							#Log Level		
	if  loglevel == 'DEBUG':
		lev=logging.DEBUG
	elif loglevel == 'INFO':
		lev=logging.INFO
	elif loglevel == 'WARNING':
		lev=logging.WARNING 
	elif loglevel == 'ERROR':
		lev=logging.ERROR 
	elif loglevel == 'CRITICAL':
		lev=logging.CRITICAL
	else: lev=100   #logging ausgeschaltet
	console.setLevel(lev)						
	logging.getLogger('basis').addHandler(console)			#add the handlers to the root logger
	return logger  

	
'''
Hauptprogramm
'''   
#INI/CFG System/Programm
sys_cfg=parse_cfg('sys.cfg')

#INI/CFG User
user_cfg=parse_cfg('user.cfg')

#log Datei 
logger=parse_logger()  

msg= 'modul %s %s' %('glb.py','ok')
logger.info(msg)




























	 


			
   