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
globale Variablen / Konstsanten
'''
  
#Globale thread variablen
#
# 'id','name','para','exit'   -> für alle Start parameter

th = {
		'0': {'id':1,'name':'main'    ,'para':None, 'exit':False, 'sys_down':''},     #hauptprogramm 
		'1': {'id':1,'name':'KEYB'    ,'para':None, 'exit':False, 'val':''},                                                                                        # Thread1 User Keypad         
		'2': {'id':2,'name':'LICHT'   ,'para':None, 'exit':False, 'name_arr':['LICHT NULL','LICHT SA','LICHT SU','LICHT MA','LICHT MU','LICHT SA','LICHT SU']},    # Thread2 Licht 
		'3': {'id':3,'name':'SOCKET'  ,'para':None, 'exit':False, 'con':False,'run':False,'status':'ini','cmd':''},                                                    # Thread3 HTTP SERVER   
		#'4': {'id':4,'name':'LED_STAT','para':None, 'exit':False},                                                                                                 # Thread4 Status LED  
	  }      

  
	  
	  
'''
global Logging
globale Konfigurations Dateien
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
 
 
def parse_logger():

	#logfile
	#
	#https://docs.python.org/2/howto/logging.html 
	#https://docs.python.org/2/library/logging.handlers.html
	#
	
	#ini values
	sec1 = sys_cfg['log']    #log section
	loglevel=sec1['loglevel'].upper()
	log_path=sys_cfg['sys']['logpathname']

	#file	
	logger = logging.getLogger()
	#log level
	if  loglevel == 'DEBUG':
		logger.setLevel(logging.DEBUG)
	elif loglevel == 'INFO':
		logger.setLevel(logging.INFO)
	elif loglevel == 'WARNING':
		logger.setLevel(logging.WARNING) 
	elif loglevel == 'ERROR':
		logger.setLevel(logging.ERROR) 
	elif loglevel == 'CRITICAL':
		logger.setLevel(logging.CRITICAL)
	else: log_level=logging.DEBUG 
	#handler file handler
	handler = logging.handlers.RotatingFileHandler(log_path,
												   maxBytes=sec1.as_int('maxbytes'),
												   backupCount=sec1.as_int('backupcount'),
												   encoding='utf-8',
												   mode='a',
												   )
	formatter = logging.Formatter(
			'%(asctime)s %(levelname)-8s %(module)-6s %(threadName)-12s %(lineno)-4s : %(message)s', datefmt='%d.%m.%Y %H:%M:%S')       
	handler.setFormatter(formatter)

	#add file
	logger.addHandler(handler)

	return logger  

'''
Hauptprogramm
'''   
print ("load glb.py")
#INI/CFG System/Programm
sys_cfg=parse_cfg('sys.cfg')
#INI/CFG User
user_cfg=parse_cfg('user.ini')
#log Datei 
#logger=parse_logger()  

logger=None




#konfiguration durch cfg file
sec1 = sys_cfg['log']    
loglevel=sec1['loglevel'].upper()
log_path=sys_cfg['sys']['logpathname']

#formatierung für alle
formatter = logging.Formatter(
			'%(asctime)s %(levelname)-8s %(module)-6s %(threadName)-12s %(lineno)-4s : %(message)s',
			datefmt='%d.%m.%Y %H:%M:%S')

#rotating file handler
rf = logging.handlers.RotatingFileHandler(log_path,
												   maxBytes=sec1.as_int('maxbytes'),
												   backupCount=sec1.as_int('backupcount'),
												   encoding='utf-8',
												   mode='a',
												   )
rf.setFormatter(formatter)

# sys.stderr
console = logging.StreamHandler()
console.setFormatter(formatter)

#add the handlers to the root logger
logging.getLogger('').addHandler(console)
logging.getLogger('').addHandler(rf)

#use the root logger for logging
logger=logging.getLogger()
#setup log level
if  loglevel == 'DEBUG':
	logger.setLevel(logging.DEBUG)
elif loglevel == 'INFO':
	logger.setLevel(logging.INFO)
elif loglevel == 'WARNING':
	logger.setLevel(logging.WARNING) 
elif loglevel == 'ERROR':
	logger.setLevel(logging.ERROR) 
elif loglevel == 'CRITICAL':
	logger.setLevel(logging.CRITICAL)
else: log_level=logging.DEBUG 



#logger.debug('Quick zephyrs blow, vexing daft Jim.')
#logger.info('How quickly daft jumping zebras vex.')
#logger.warning('Jail zesty vixen who grabbed pay from quack.')
#logger.error('The five boxing wizards jump quickly.')



































	 


			
   