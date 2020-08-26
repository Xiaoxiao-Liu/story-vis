# coding:utf-8
import jieba
from .config import OUTPUT_PATH,STOPWORD_PATH
from .uils import remove_punctuation,stopwordslist,greeting
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

stopwords = stopwordslist(STOPWORD_PATH)

title_list = []

with open(OUTPUT_PATH,'r',encoding='utf-8') as fr:
    for title in fr.readlines():
        title_list.append(title.replace('\n',''))

# 列表故事去重
title_list = list(set(title_list))

# 删除除字母,数字，汉字以外的所有符号
df = pd.DataFrame(title_list, columns=['sent'])
df['clean_set'] = df['sent'].apply(remove_punctuation)

# 分词，并过滤停用词
df['cut_sent'] = df['clean_set'].apply(lambda x: " ".join([w for w in jieba.lcut(x)]))

# 机器应答设计
def response(user_response):
    robo_response = []

    # 将用户的提问去除特殊符号并分词
    user_response = remove_punctuation(user_response)
    user_response = " ".join([w for w in jieba.lcut(user_response) if w not in stopwords])

    cut_sent = df['cut_sent'].values.tolist()
    cut_sent.append(user_response)
    tfidf = TfidfVectorizer()
    tfidf_vec = tfidf.fit_transform(cut_sent)

    """cosine_similarity的用法"""
    # 余弦相似度                 最后一个词    所有的分词后的句子
    cos_sim = cosine_similarity(tfidf_vec[-1], tfidf_vec)
    # 将求得的相似度进行索引排序 取倒数第二个值(id) 是最相似的，此时
    idx_1 = cos_sim.argsort()[0][-2]   # 这里只是取索引，顺序并没有改变
    idx_2 = cos_sim.argsort()[0][-3]
    idx_3 = cos_sim.argsort()[0][-4]
    idx_4 = cos_sim.argsort()[0][-5]
    # 将cos_sim 展开成一维数组，即句子的相似度，用于判断
    flat = cos_sim.flatten()
    # 将相似度进行排序
    flat.sort()
    # 取最相似的句子的值
    req_tfidf = flat[-2]
    robo_response.append(df.sent.values[idx_1])
    robo_response.append(df.sent.values[idx_2])
    robo_response.append(df.sent.values[idx_3])
    robo_response.append(df.sent.values[idx_4])
    title_list.pop()
    return robo_response

def main_mod(request):
    user_response = request
    user_response = user_response.lower()
    return response(user_response)

# print(main_mod('王子和公主'))

# flag = True
# print("机器人: 我的名字叫小白. 我可以回答您关于5G的问题. 如果您想退出, 请输入:bye !")
#
# while (flag == True):
#     user_response = input('问：')
#     user_response = user_response.lower()
#     if (user_response != 'bye'):
#         if (user_response == '多谢' or user_response == '谢谢'):
#             flag = False
#             print("机器人: 不用谢！")
#         else:
#             if (greeting(user_response) != None):
#                 print("机器人: " + greeting(user_response))
#                 print()
#             else:
#                 print("机器人: ", end="")
#                 print(response(user_response))
#                 print()
#     else:
#         flag = False
#         print("小白: 再见! 欢迎再次光临!")

