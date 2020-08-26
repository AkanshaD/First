import shutil
import sys
import os.path
from os import path

src = sys.argv[1]
dest = sys.argv[2]

#Displaying paths
print("Source : " +src)
print("Destination: " +dest)

#Checks for destination validity
if path.isdir(dest)==0:
    print("Such a destination does not exist!")
    print("Ending operation")
    exit()      #Ending program

print("-------------------------------")
print("Moving files\n")
print("-------------------------------")

#Code logic
files=[src+"\File1.txt",src+"\File2.txt",src+"\File3.pptx"]
for f in files:
    shutil.move(f,dest)
    
#Displaying completion acknowledgement 
print("Successfully done.")
