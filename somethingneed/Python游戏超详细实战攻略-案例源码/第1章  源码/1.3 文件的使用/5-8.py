import os
totalSize=0
os.chdir("d:\\python")
for fileName in os.listdir(os.getcwd()):
	totalSize+=os.path.getsize(fileName)
print( totalSize)


