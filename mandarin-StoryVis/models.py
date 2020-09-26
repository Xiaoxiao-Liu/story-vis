from pymysql import *
import jieba.posseg as pseg
import pandas as pd
import color_generatior as cg
import json
conn = connect(host='121.40.208.170', port=3306, user='root', password='123456', database='Text_Project')
cur=conn.cursor()

#获取故事内容
def emo_sql_read(title):
    # 获得cursor对象
    #emo_cursor = conn.cursor()
    sql_1_1 = "SELECT distinct  w.word, w.chinese_emotion, w.p_n FROM word_table w,sentence_table s,text_table t where w.sentence_id=s.sentence_id and s.text_id=t.text_id and w.p_n is not null and t.text_title='" + title + "';"
    cur.execute(sql_1_1)
    story_data = cur.fetchall()
    return story_data

def data_transform(title):
    # Transfrom tuple of the data into dataframe
    emo_data = emo_sql_read(title)
    tuple_to_list =  list(map(lambda x: list(x), list(emo_data)))
    columns = ['word','chinese_emotion','p_n']
    emotion_df = pd.DataFrame(tuple_to_list,columns=columns)
    return emotion_df


def get_emotions(emotion_df,emotion,title):
    # Get title-emotions dict
    emotion_dict = {}
    ## cut the dataframe for negative/positive emotions
    emo_df = emotion_df.loc[emotion_df['p_n'] == emotion]
    ## get the emotion list
    emotion_arr = list(emo_df['chinese_emotion'].unique())
    emotion_dict[title] = list(emotion_arr)
    # Get emotions-words dict
    emoword_dict = emo_df.groupby('chinese_emotion')['word'].apply(list).to_dict()
    emo_no = len(list(emotion_dict.values())[0])
    return emotion_dict,emoword_dict,emo_no

def data_for_vis(title):
    emotion_df = data_transform(title)
    # Get negative visualization data
    title_neg, neg_word,neg_no = get_emotions(emotion_df, '负面词性', title)
    # Get negative color Hex codes
    cg.input_colors = ["#79CBCA", "#77A1D3"]
    neg_colors = cg.gradient_color(cg.input_colors, neg_no)  # 负
    # Get positive visualization data
    title_pos,pos_word,pos_no = get_emotions(emotion_df, '正面词性', title)
    # Get positive color Hex codes
    cg.input_colors = ["#E684AE", "#79CBCA"]
    pos_colors = cg.gradient_color(cg.input_colors, pos_no)  # 正
    return title_neg, title_pos,pos_word,neg_word,title,pos_colors,neg_colors

#词性配色
def emo_sql_read_2(title):
    # 获得cursor对象
   # sql_3="SELECT distinct w.word,w.chinese_emotion,w.p_n FROM word_table w,sentence_table s,text_table t where w.sentence_id=s.sentence_id and s.text_id=t.text_id and w.p_n is not null and t.text_title='"+title+"';"
    p_nums = []
    pro_nums=[]
    sql_9="SELECT w.chinese_property,COUNT(*) from word_table w,sentence_table s,text_table t WHERE w.sentence_id=s.sentence_id and s.text_id=t.text_id and t.text_title='"+title+"' GROUP BY w.chinese_property order by COUNT('w.chinese_property') desc;"
    cur.execute(sql_9)
    # for row in cur.fetchall():
    #     print(row)
    #     p_nums.append(row[1])
    # print(p_nums)
    # for i in p_nums:                #循环数据，将数据做归一化处理，处理结果控制在0-1的范围里面
    #     #all=round((float(i)-min(p_nums))/float(max(p_nums)-min(p_nums)),3)#归一化公式，并将值保留小数点后三位
    #     pro_nums.append(all)
    # print(pro_nums)
    story_data = cur.fetchall()
    #print(story_data)
    return story_data

#这一部分开始对情感分析可视化进行颜色跟词语匹配分析
def data_transform_2(title):
    # Transfrom tuple of the data into dataframe
    emo_data = emo_sql_read_2(title)

    tuple_to_list =  list(map(lambda x: list(x), list(emo_data)))
    columns = ['word','chinese_emotion']
    emotion_df = pd.DataFrame(tuple_to_list,columns=columns)
    #print(emotion_df)
    return emotion_df

#这一部分开始对情感分析可视化进行颜色跟词语匹配分析
def get_emotions_2(emotion_df,title):
    # Get title-emotions dict
    emotion_dict = {}
    emotion_arr = list(emotion_df['chinese_emotion'])
    emotion_dict[title] = list(emotion_arr)
    # Get emotions-words dict
    emoword_dict = emotion_df.groupby('chinese_emotion')['word'].apply(list).to_dict()
    emo_no = len(list(emotion_dict.values())[0])
    #print(emotion_dict)

    return emotion_dict,emoword_dict,emo_no
#这一部分开始对情感分析可视化进行颜色跟词语匹配分析
def data_for_vis_2(title):
    emotion_df = data_transform_2(title)
    # Get positive visualization data
    title_pos,pos_word,pos_no = get_emotions_2(emotion_df, title)

    # Get positive color Hex codes
    cg.input_colors = ["#9795f0", "#fbc8d4"]
    pos_colors = cg.gradient_color(cg.input_colors, pos_no)  # 正
    #print("2",pos_colors)
    return pos_colors
    #return title_pos, title_pos,pos_word,pos_word,title,pos_colors,pos_colors

def models_mysql(title):
    #词性饼图的列表
    propertys=[]    #所有词性与次数的列表
    pro_name=[]     #所有词性的中文名字
    pro_number=[]   #所有词性的出现的次数
    pro_num=[]      #所有词性经过归一化处理后的数值

    #雷达图的列表
    entropy_num=[]  #5个熵的值
    entropy_number=[]

    #词云的列表
    readability_num_1=[]
    readability_num_2 = []
    readability_num_3 = []
    readability_num_4 = []
    readability_num_5 = []
    readability_num_6 = []
    readability_num_7 = []
    readability_num_8 = []
    readability_num_9 = []


    #词性图
    #选择单词
    word=[]
    sql_10="SELECT w.word from word_table w,sentence_table s,text_table t WHERE w.chinese_property='名词' and w.sentence_id=s.sentence_id AND s.text_id=t.text_id AND t.text_title='"+title+"'  GROUP BY w.word order by COUNT('w.word') desc limit 0,50;"
    cur.execute(sql_10)
    for i in cur.fetchall():
        word.append(i[0])
    #print(word)
    #sql_1="SELECT w.chinese_property,COUNT(*) from word_table w,sentence_table s,text_table t WHERE w.sentence_id=s.sentence_id and s.text_id=t.text_id and t.text_title='"+title+"' GROUP BY w.chinese_property order by COUNT('w.chinese_property') desc limit 0,8;"
    sql_1="SELECT w.chinese_property,COUNT(*),p.emotion from p_c p,word_table w,sentence_table s,text_table t WHERE w.sentence_id=s.sentence_id and s.text_id=t.text_id and p.chinese=w.chinese_property and t.text_title='"+title+"' GROUP BY w.chinese_property order by COUNT('w.chinese_property') desc;"
    cur.execute(sql_1)
    pro_names=[]
    proname = []
    pn_color=[]
    for row in cur.fetchall():
        propertys.append({row[0]:row[1]})    #将数据库w.chinese_property,COUNT(*)数据以字典的形式存放在列表里面
        pro_names.append(row[0])             #列表里面添加w.chinese_property
        pro_num.append(row[1])           #列表里面添加COUNT(*)
        pn_color.append(row[2])
    # print(pn_color)
    for i in pro_names:
        if i=="地名":
            proname.append("专属名词")
        else:
            proname.append(i)
    pro_name=list(set(proname))
    length_p = len(pro_name)    #获得列表长度

    # 雷达图数据
    sql_2 = "SELECT emtion_entropy,property_entropy,importance_entropy,strokes_entropy,strokes_16_pro FROM text_table WHERE text_title='"+title+"';"
    cur.execute(sql_2)
    for row in cur.fetchall():
        for i in row:
            entropy_num.append(i)
    #print(entropy_num)

    #词云图数据
    sql_3="SELECT r.* from readability_table r,text_table t where t.text_id=r.text_id and t.text_title='"+title+"';"
    cur.execute(sql_3)
    for row in cur.fetchall():
        #importance_name.append(row[0])  #添加w.word数据到列表
        readability_num_1.append(row[1])   #添加w.importance数据到列表
        readability_num_2.append(row[2])
        readability_num_3.append(row[3])
        readability_num_4.append(row[4])
        readability_num_5.append(row[5])
        readability_num_6.append(row[6])
        readability_num_7.append(row[7])
        readability_num_8.append(row[8])
        readability_num_9.append(row[9])
    #length_i=len(importance_name)       #获得列表长度
    #print(readability_num_5)

    #主角图片
    img_name=[]
    words=[]
    sql_4="SELECT img_name from text_table WHERE text_title='"+title+"';"
    cur.execute(sql_4)
    for row in cur.fetchall():
        words=row[0]

    for array in words.split():
        img_name.append(array)
    #print(img_name)
    imgs=len(img_name)
    #print(imgs)

    #文章内容
    sql_6="SELECT c.text_content FROM text_content_table c JOIN (SELECT * FROM text_table WHERE text_title = '"+title+"') t ON t.text_id =.c.text_id;"
    cur.execute(sql_6)
    for row in cur.fetchall():
        content=str(row[0])
    #print('changdu',len(content))
    all_num = []
    lenght = len(content)
        # print(lenght)
    # 计算文章分为5部分的字数
    for i in range(1, 6):
        num = int((lenght * (i / 5)))
        all_num.append(num)
    #print(all_num)

    #甜甜圈配色
    #正面
    sql_18="SELECT distinct w.chinese_emotion,c.c4 from word_table w,sentence_table s,text_table t,color_table c WHERE w.sentence_id=s.sentence_id AND s.text_id=t.text_id and t.text_title='"+title+"' AND w.chinese_emotion=c.`name` AND w.p_n='正面词性';"
    cur.execute(sql_18)
    tcolor=[]
    for row in cur.fetchall():
        tcolor.append(row[1])
    #print('t',tcolor)

    #负面
    sql_19 = "SELECT distinct w.chinese_emotion,c.c4 from word_table w,sentence_table s,text_table t,color_table c WHERE w.sentence_id=s.sentence_id AND s.text_id=t.text_id and t.text_title='" + title + "' AND w.chinese_emotion=c.`name` AND w.p_n='负面词性';"
    cur.execute(sql_19)
    fcolor = []
    for row in cur.fetchall():
        fcolor.append(row[1])
    #print('f',fcolor)
    # 情感词的条形图配色
    sql_20="SELECT c4 from color_table;"
    cur.execute(sql_20)
    all_color=[]
    for row in cur.fetchall():
        all_color.append(row[0])
    #print(all_color)

    # 摘要数据
    '''
    sql_21="SELECT abstract from text_content_table"
    cur.execute(sql_21)
    all_abstract = []
    for abstract in cur.fetchall():
        print(abstract)
        all_abstract.abstract(row[0])
    '''
    #print(all_abstract)

    return pn_color,content,all_color,fcolor,tcolor,all_num,word,imgs,img_name,propertys,pro_name,pro_number,pro_num,entropy_num,readability_num_1,readability_num_2,readability_num_3,readability_num_4, readability_num_5,  readability_num_6, readability_num_7, readability_num_8, readability_num_9,length_p



'''
if __name__ == '__main__':
    title = "骗子与商人"
    data_for_vis(title)
    models_mysql(title)
'''



