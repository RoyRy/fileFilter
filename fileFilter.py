'''
Description: 
version: 1.0.0
Author: yuanruiyi
Date: Thu, 23 Feb 2023 09:57:00
LastEditors: hefulai
LastEditTime: Thu, 23 Feb 2023 09:57:00 
todo: 筛选图片中有对应xml标签的图片
'''
# 使用方法：python fileFilter.py path1 path2 path3
# -path1 被筛选文件夹 
# -path2 对照文件夹 
# -path3 保存文件夹

import os
import glob
import sys
from rich.progress import track
import cv2

def dirlist(path, allfile):  
    filelist =  os.listdir(path)  
  
    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath):  
            dirlist(filepath, allfile)  
        else:  
            allfile.append(filepath)  
    return allfile  
  
folderPath1 = sys.argv[1] 
filePath1 = []
fileName1 = []
dirlist(folderPath1, filePath1)
print("被筛选文件夹：" + folderPath1)

folderPath2 = sys.argv[2]  
filePath2 = []
fileName2 = []
dirlist(folderPath2, filePath2)
print("对照文件夹：" + folderPath2)

folderPath3 = sys.argv[3]
print("保存文件夹：" + folderPath3)

#遍历所有文件，获取文件名称（包括后缀）
for item in filePath1:
    fileName1.append(os.path.basename(item).split('.')[0])

for item in filePath2:
    fileName2.append(os.path.basename(item).split('.')[0])

#通过遍历，获取第一个文件夹下，文件名称（不包括后缀）与第二个文件夹相同的文件，并另存在outDir文件夹下。文件名称与第一个文件夹里的文件相同，后缀格式亦保持不变。
for item2 in track(fileName2):
    for item1 in fileName1:
        if item1 == item2:
            path_in = str(folderPath1) + item1 +".jpg"
            img = cv2.imread(str(path_in))
            # 显示当前图片
            # cv2.imshow("temp",img)
            # cv2.waitKey(1)
            path_out =  str(folderPath3) + item1 + ".jpg"
            print(path_out)
            cv2.imwrite(path_out, img)
    



