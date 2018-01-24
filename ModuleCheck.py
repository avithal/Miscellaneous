""" Checking modules in a  system"""
import sphinx
import sys
print (sphinx.__version__ )
modulename = "numpy"
if modulename not in sys.modules:
   print("You have not imported the {} module:" + modulename)
