helloFile=open("d:\\python\\hello.txt")
fileContent=""
while True:
	line=helloFile.readline()
	if line=="":    # 或者 if not line
	    break
	fileContent+=line
helloFile.close()
print(fileContent)

