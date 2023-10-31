import os
list_dirs = os.walk("H:\档案科技表格")                 #返回一个元祖
print(list(list_dirs))
for folderName,subFolders,fileNames in list_dirs:
	print("当前目录：" + folderName)
	for subFolder in subFolders:
		print(folderName +"的子目录" + " 是--" + subFolder)
		for fileName in fileNames:
			print(subFolder +"的文件 " +  " 是--" + fileName)



