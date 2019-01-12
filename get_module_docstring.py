#!/usr/bin/env python

__author__ = 'Jake Miller (@LaconicWolf)'
__date__ = '20190111'
__version__ = '0.01'
__description__ = '''Returns names and docstring of objects within a module'''

import sys
import inspect

if len(sys.argv) != 2:
    print("Usage: python {0} <name of module>\nExample: python3 {0} requests".format(sys.argv[0]))
    exit()

module = __import__(sys.argv[1])

for object, value in inspect.getmembers(module):
    if not object.startswith('_'): 
            print("=" * 55)
            try:                   
                    print(object, inspect.getdoc(module.__getattribute__(object)))
            except Exception as e:  
                    print(object, e)
            print("=" * 55 + '\n')