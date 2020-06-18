#/!\ It's important to respect quoting marks#

	#To import the package :
from Saving import dumping,loading
	
	#To save the variable B in file Save.txt (if Save.txt doesn't exist, it'll be created) :
dumping(B,"Save.txt")

	#To load the variable B from the doc Save.txt :
B = loading("B","Save.txt")

