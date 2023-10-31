def copy_file(oldfile,newfile):
	oldFile=open(oldfile,"r")
	newFile=open(newfile,"w")
	while True:
		fileContent=oldFile.read(50)
		if fileContent=="":
			break
		newFile.write(fileContent)
	oldFile.close()
	newFile.close()
	return
copy_file("d:\\python\\hello.txt","d:\\python\\hello2.txt")





