#! /usr/bin/env python3

path = "/mnt/e/5/"

# 查找第一个空格，将之前所有字符替换为dst_str
src_str = " "
dst_str = ""

#挂载硬盘
#sudo mount -t drvfs E: /mnt/e
#弹出硬盘
#sudo umount /mnt/e

#判断是否文件
#if os.path.isfile(path_file_name)) == True:
#判断是否目录
#if os.path.isdir(path_file_name)) == True:

import os
for file_name in os.listdir(path):
#路径+文件名
	path_file_name = os.path.join(path, file_name)
#判断是否文件
	if os.path.isfile(path_file_name) == False:
		continue
	pos = file_name.find(src_str)
	if pos == -1:
		continue
	new_path_file_name = os.path.join(path, file_name[pos + 1:])
#判断文件是否存在
	if os.path.exists(new_path_file_name) == True:
		print(f"{path_file_name} rename {new_path_file_name} fail for exist")
		continue
#重命名
	os.rename(path_file_name, new_path_file_name)
	print(f"{path_file_name} rename {new_path_file_name} success")
