import re
import jieba
import json
from pymysql import *


class Dw(object):
    def __init__(self):

        conn = connect(host='121.40.208.170', port=3306, user='root', password='123456', database='Text_Project')
        # 如上代码：连接数据库
        self.emo_cursor = conn.cursor()
        # 获得cursor对象

    def __sql_read(self, title):  # 创建读取数据库的函数

        self.emo_cursor.execute(
            'SELECT tc.text_content FROM text_table t,text_content_table tc where t.text_id=tc.text_id and t.text_title="%s";' % title)
        # 如上代码：查询数据库word_table，text_table表（目的：查询出每个故事的内容）

        story_data = self.emo_cursor.fetchall()

        # 返回元组
        return story_data

    def __sql_read2(self, title):  # 创建读取数据库的函数

        self.emo_cursor.execute(
            'SELECT w.word ,w.chinese_property FROM text_table t,sentence_table s,word_table w where t.text_id=s.text_id and s.sentence_id=w.sentence_id and t.text_title="%s";' % title)
        # 如上代码：查询数据库word_table，text_table表（目的：查询出每个故事的内容）
        story_data = self.emo_cursor.fetchall()
        print("sto:",story_data)

        # 返回元组
        return story_data

    def fen(self, title, page):  # 创建分页的函数，需要输入故事名称，页数

        self.dict_page = {}
        content_data = self.__sql_read(title)  # 接收查询故事内容
        # print(content_data)
        content_data2 = self.__sql_read2(title)
        # print(content_data2)

        if page in [5, 10, 15, 20]:
            # print(11111111111111111111111111)
            if content_data:  # 判断是否有这个故事
                content_data = content_data[0]  # 故事内容
                start = 0
                size = len(content_data[0]) // page + 1  # 按照传入的页数把故事内容平分

                for i in range(1, page + 1):  # 按照每页字数+标点数进行分页
                    self.dict_page.update({'page_%d' % i: content_data[0][start:start + size]})  # 将分页加入字典
                    start += size

            else:
                print("没有这个故事！！！")

            # print(self.dict_page)
            return self.dict_page, content_data2  # 返回整个分页字典

        else:
            if content_data:  # 判断是否有这个故事
                content_data = content_data[0]  # 故事内容
                #print(content_data[0])
                start = 0
                size = len(content_data[0]) // page + 1  # 按照传入的页数把故事内容平分

                for i in range(1, size + 1):  # 按照每页字数+标点数进行分页
                    self.dict_page.update({'page_%d' % i: content_data[0][start:start + page]})  # 将分页加入字典
                    start += page
            else:
                print("没有这个故事！！！")

            #print(self.dict_page)
            return self.dict_page, content_data2  # 返回整个分页字典




    def cixing(self, title, page):  # 创建分页and分析情感的函数，需要输入故事名称，页数

        self.fen_data = self.fen(title, page)  # 调用分页函数
        # print(fen_data[0])
        # print(fen_data[1])
        cixing_dict = {}
        for i in self.fen_data[1]:
            # print(i[0])
            # print(i[1])
            cixing_dict[i[0]] = i[1]

        quan_bu_ci_xing = []
        self.page_dict_cixing = {}
        for i in range(1, len(self.fen_data[0]) + 1):  # 将分页的故事内容一页一页的进行分词，

            re_tetx = re.sub(r'[，|。|、|：|“|”|？|！|;|\,|\.|\"|\"|:]*', '', self.fen_data[0]['page_' + str(i)])  # 去除标点符号
            text_list = jieba.lcut(re_tetx)  # 分词，返回列表
            # print(text_list)
            page_data = []
            for j in text_list:
                if j in cixing_dict.keys():
                    page_data.append(cixing_dict[j])
                    quan_bu_ci_xing.append(cixing_dict[j])
                    self.page_dict_cixing['page_%d' % i] = page_data
            # print(page_data)
        # print(len(list(set(quan_bu_ci_xing))))
        # print(page_dict_cixing)

        cixing_dict_2 = {}
        for i in list(set(quan_bu_ci_xing)):  # 构造词性字典
            # print(i)
            cixing_dict_2[i] = 0
        #print(cixing_dict_2)

        cixing_dict_3 = {}
        for i in list(set(quan_bu_ci_xing)):  # 构造词性字典
            cixing_dict_3[i] = []
        # print(cixing_dict_3)

        # print(11111111111111111111)
        for k in self.page_dict_cixing.values():
            for i in cixing_dict_2.keys():
                if i in k:
                    count_1 = k.count(i)
                    cixing_dict_2[i] = count_1

            for x in list(cixing_dict_2.keys()):
                cixing_dict_3[x].append(cixing_dict_2[x])
        # yield list(PN_dict.values())
        # print(cixing_dict_3)
        return cixing_dict_3  # 返回这个故事的所有词性在每一页的次数

    def page_cixing(self):
        return self.page_dict_cixing  # 返回每一页的词性

    def ding_wei(self,title,page,ciyu):
        self.cixing(title,page)
        a_dict={}
        b_dict_data={}
        page_list=[]
        for i in self.fen_data[1]:
            #print(i)
            if ciyu in i[0]:
                lenthe=i[1]
                if lenthe=="地名":
                    lenthe='专属名词'
                b_dict_data['lenthe']=lenthe
                break
        else:
            lenthe = '-1'
            b_dict_data['lenthe'] = lenthe

        for j in self.dict_page:
            #print(j)
            if ciyu in self.dict_page[j]:
                page_list.append(j.split('_')[1])
                #print(j.split('_')[1])

        b_dict_data['page'] = page_list

        if b_dict_data['lenthe'] != '-1' and b_dict_data['page'] != '-1':
            msg = '获取成功'
            code='201'
            a_dict['data'] = b_dict_data
            a_dict['msg'] = msg
            a_dict['code'] = code
        else:
            msg = '获取失败'
            code = '500'
            a_dict['data'] = b_dict_data
            a_dict['msg'] = msg
            a_dict['code'] = code
        print(a_dict)
        return a_dict





# a = Dw()  # 创建对象
#print(a.fen('狐狸和乌鸦的故事',30))
# print(a.cixing())
#print(a.page_cixing())
# print(a.ding_wei('狐狸和乌鸦的故事',1000,'狐狸'))

