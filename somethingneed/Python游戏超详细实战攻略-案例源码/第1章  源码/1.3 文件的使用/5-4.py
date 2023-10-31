helloFile=open("d:\\python\\hello.txt")
fileContent=helloFile.readlines()
helloFile.close()
print(fileContent)
for line in fileContent:   #输出列表
   print(line)



