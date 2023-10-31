helloFile=open("d:\\python\\hello.txt")
fileContent=""
while True:
	fragment=helloFile.read(3)
	if not fragment:
		break
	fileContent+=fragment
helloFile.close()
print(fileContent)

