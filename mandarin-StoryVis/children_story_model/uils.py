# coding:utf-8
import os
import re
import random
import jieba

# 判断是否有保存路径，若没有，创建目录和文件
def is_dir(path):
    PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)),path)
    if not os.path.exists(PATH):
        print(PATH)
        os.mkdir(PATH)
        file = open('{}/童话.txt'.format(PATH),'w')
        file.close()
    else:
        print("文件夹已存在")
        file = open('{}/童话.txt'.format(PATH),'w')
        file.close()

#删除所有符号,只保留字母、数字和中文
def remove_punctuation(line):
    #line = str(line)
    if line.strip() == '':
        return ''
    rule = re.compile(u"[^a-zA-Z0-9\u4E00-\u9FA5]")
    line = rule.sub('',line)
    return line


def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

# 问候语设计
user_input = ("你好", "hai", "有人", "在吗", "嗨", "在不在", "有人吗", '在', '有人','好','hi')
bot_response = ["你好", "我在", "请问,有什么可以帮您的吗?", "你好，我在", "你好，很高兴见到你！"]
def greeting(sentence):
    text = remove_punctuation(sentence)
    if text in user_input:
        return random.choice(bot_response)

    wordlist = [w for w in jieba.cut(sentence)]
    for word in wordlist:
        if word in user_input:
            return random.choice(bot_response)
