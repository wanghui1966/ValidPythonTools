#! /usr/bin/env python3


path = "/mnt/d/按卷更新/"
src_str = "【时未寒】"
dst_str = "时未寒"

#path = "./"
#src_str = "[飘花电影网]"
#dst_str = ""

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
	new_path_file_name = os.path.join(path, file_name.replace(src_str, dst_str))
#判断文件是否存在
	if os.path.exists(new_path_file_name) == True:
		print(f"{path_file_name} rename {new_path_file_name} fail for exist")
		continue
#重命名
	os.rename(path_file_name, new_path_file_name)
	print(f"{path_file_name} rename {new_path_file_name} success")
