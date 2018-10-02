# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
globale Funktionen
"""

#std
import inspect
import ntpath

#eigene  
import glb
from glb import sys_cfg,user_cfg,logger     # cfg parameter, logger
import bas


def path_leaf(path):
	#
	#trennt pfad vom pfad und dateinamen ab
	# 
	#
	head, tail = ntpath.split(path)
	return tail or ntpath.basename(head)
	

def mod_name(): 
	#
	#name des moduls
	#   
	#
	st=inspect.stack()
	return path_leaf(st[1][1])

msg= 'modul %s %s' %(mod_name(),'ok')
logger.info(msg)	 
	 



	
	
	
	
	
	
	
	