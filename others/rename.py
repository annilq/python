# 来源
# https://www.jianshu.com/p/c6ad6a896b1d
import os
dir = os.getcwd()         #获取当前目录
# subdir = os.listdir(dir)  #遍历当前目录下所有文件，也就是获取第一级作者名字所有文件夹
# os.path.join(dir,i)      #把第一级目录添加到路径中
# os.path.isdir(path):         #如果path仍然是文件夹，下面就继续遍历出其中的文件，
def rename(dir):
	for file in os.listdir(dir):
		if file[-2:]=="py":
			continue
		name = file.replace(' ', '').split("-")[0]
		newname="emoji_"+name+".png"
		print(newname)
		os.rename(file, newname)

# 更改当前目录文件名
dir = os.getcwd() 
rename(dir)
