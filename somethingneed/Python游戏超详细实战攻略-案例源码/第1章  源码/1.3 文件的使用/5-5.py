helloFile=open("d:\\python\\hello.txt","w")
helloFile.write("First line.\nSecond line.\n")
helloFile.close()
helloFile=open("d:\\python\\hello.txt","a")
helloFile.write("third line. ")
helloFile.close()
helloFile=open("d:\\python\\hello.txt")
fileContent=helloFile.read()
helloFile.close()
print(fileContent)




