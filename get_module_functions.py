import sys
import inspect

if len(sys.argv) != 2:
    print("Usage: python {0} <name of module>\nExample: python3 {0} requests".format(sys.argv[0]))
    exit()

module = __import__(sys.argv[1])

for object, value in inspect.getmembers(module, inspect.isfunction):
    if not object.startswith('_'): # Exclude internal or dunder methods
            try:                   # Prints functions that don’t require params
                    print(object, module.__getattribute__(object)())
            except Exception as e: # Prints functions that require params 
                    print(object, e)