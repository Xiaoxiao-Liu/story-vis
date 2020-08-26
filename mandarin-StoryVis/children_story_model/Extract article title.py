# coding:utf-8
from config import INPUT_PATH,OUTPUT_PATH
from uils import is_dir
import os
import re

list_ = os.listdir(INPUT_PATH)

title_list = []

for lis in list_:
    path = INPUT_PATH + '\\' +lis
    with open(path,'r',encoding='utf-8') as fr:
        line = "".join(fr.readlines())
        title_list_ = re.findall('(题目：|题目 ：)(.*?)\n', line)
        for title in title_list_:
            try:
                if len(title[1]) <= 20:
                    title_list.append(title[1])
            except:
                continue

is_dir('data/童话数据集')

for title in title_list:
    with open(OUTPUT_PATH,'a',encoding='utf-8') as fw:
        fw.writelines(title+'\n')
print('保存成功')