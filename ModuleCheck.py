""" Checking modules in a  system"""
import sphinx
import sys
print(sphinx.__version__)
module_name = "numpy"
if module_name not in sys.modules:
    print("You have not imported the {} module:" + module_name)
