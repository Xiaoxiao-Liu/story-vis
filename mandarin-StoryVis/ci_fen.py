import re
import jieba
import json

from pymysql import *


class Word(object):
    def __init__(self):

        conn = connect(host='121.40.208.170', port=3306, user='root', password='123456', database='Text_Project')
        # 如上代码：连接数据库
        self.emo_cursor = conn.cursor()
        # 获得cursor对象
        with open("资料/PN_text.json", 'r', encoding='utf-8') as f:  # 正负词性的json文件
            self.qinggan_dict = json.load(f)  # 情感词字典

    def __sql_read(self, title):  # 创建读取数据库的函数

        self.emo_cursor.execute(
            'SELECT tc.text_content FROM text_table t,text_content_table tc where t.text_id=tc.text_id and t.text_title="%s";' % title)
        # 如上代码：查询数据库word_table，text_table表（目的：查询出每个故事的内容）

        story_data = self.emo_cursor.fetchall()

        # 返回元组
        return story_data

    def ci_fen(self, title, size):  # 创建分页的函数，需要输入故事名称，页数
        self.dict_page = {}
        content_data = self.__sql_read(title)  # 接收查询故事内容

        if content_data:  # 判断是否有这个故事
            self.content_num= content_data[0]  # 故事字数
            content_data = content_data[0]  # 故事内容
            start = 0
            page = len(content_data[0]) // size + 1  # 按照传入的页数把故事内容平分

            for i in range(1, page + 1):  # 按照每页字数+标点数进行分页
                self.dict_page.update({'page_%d' % i: content_data[0][start:start + size]})  # 将分页加入字典
                start += size

        else:
            self.content_num ='NaN'  # 故事字数
            print("没有这个故事！！！")

        # print(self.dict_page)
        return self.dict_page  # 返回整个分页字典

    def ci_qinggan(self, title, page):  # 创建分页and分析情感的函数，需要输入故事名称，页数
        fen_data = self.ci_fen(title, page)  # 调用分页函数
        # print(fen_data)
        self.zheng_sum = 0
        self.fu_sum = 0

        self.all_list = []

        PN_list_dict = {'PH': [], 'PA': [], 'PD': [], 'PB': [], 'PG': [], 'PC': [],
                        'PF': [], 'PE': [], 'PK': [], 'NN': [], 'NE': [], 'ND': [],
                        'NB': [], 'NC': [], 'NH': [], 'NI': [], 'NJ': [], 'NG': [],
                        'NK': [], 'NL': []}

        for i in range(1, len(fen_data) + 1):  # 将分页的故事内容一页一页的进行分词，提取情感词
            re_tetx = re.sub(r'[，|。|、|：|“|”|？|！|\,|\.|\"|\"|:]*', '', fen_data['page_' + str(i)])  # 去除标点符号
            text_list = jieba.lcut(re_tetx)  # 分词，返回列表

            zheng_dict = {}
            # fu_dict = {}
            PN_dict = {'PH': 0, 'PA': 0, 'PD': 0, 'PB': 0, 'PG': 0, 'PC': 0,
                       'PF': 0, 'PE': 0, 'PK': 0, 'NN': 0, 'NE': 0, 'ND': 0,
                       'NB': 0, 'NC': 0, 'NH': 0, 'NI': 0, 'NJ': 0, 'NG': 0,
                       'NK': 0, 'NL': 0}  # 去除了NA

            for j in text_list:  # 将一页的分词列表遍历，提取情感词保存到zheng_dict中

                if j in self.qinggan_dict['P'].keys():
                    count_1 = text_list.count(j)  # 返回情感词出现的次数
                    zheng_dict[j] = count_1

                    p_num = PN_dict[self.qinggan_dict['P'][j]] + count_1
                    PN_dict[self.qinggan_dict['P'][j]] = p_num
                    # PN_dict[self.qinggan_dict['P'][j]]=sum

                    self.zheng_sum += count_1
                elif j in self.qinggan_dict['N'].keys():
                    count_2 = -(text_list.count(j))
                    zheng_dict[j] = count_2

                    N_num = PN_dict[self.qinggan_dict['N'][j]] + count_2
                    PN_dict[self.qinggan_dict['N'][j]] = N_num

                    self.fu_sum += count_2

            self.all_list += list(PN_dict.values())

            # print(PN_dict)

            for k in list(PN_dict.keys()):
                PN_list_dict[k].append(PN_dict[k])
            # yield list(PN_dict.values())
        return PN_list_dict
        # print(PN_list_dict)

    # P_list=[ 'PH', 'PA', 'PD', 'PB', 'PG','PC', 'PF', 'PE', 'PK', 'PH ']
    # N_list=['NN', 'NE', 'ND', 'NB', 'NC', 'NH', 'NI', 'NJ', 'NG', 'NK', 'NL']

    def qinggan_number(self):  # 创建情感词数量的函数
        print(self.zheng_sum)
        print(self.fu_sum)

    def max(self):  # 最大值最小值
        return max(self.all_list)

    def min(self):
        return min(self.all_list)
    # 这里的最大值最小值函数，是基于qinggan()这个函数的，
    # 由于qinggan()这个函数是统计这个词的情感类别在这一页出现的次数（根据分页数的不同，词的情感类别出现的次数也不同）
    # 所以，这里的最大值最小值会随着分页数的不同而产生变化

    def num(self):  # 故事字数，
        """
        如果有这个故事，返回故事字数
        如果没有这个故事，就不返还
        :return:
        """
        #print(self.content_data[0])
        all_num=[]
        if self.content_num !='NaN':
            lenght=len(self.content_num[0])
            #print(lenght)
            for i in range(1,6):
                num=int((lenght*(i/5)))
                all_num.append(num)
        return  all_num

# a = Word()
#
# print(a.ci_fen('狐狸和乌鸦的故事', 80))
# #
# print(a.ci_qinggan('狐狸和乌鸦的故事', 80))
#
# print('klj',a.num())

