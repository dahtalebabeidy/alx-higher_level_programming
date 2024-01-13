#!/usr/bin/python3
'''module for lookup method.'''

def lookup(obj):
	'''list object atributs and methods
	Args:
		obj: object
	Return:
		list of atributs and methods
	'''
	return dir(obj)
