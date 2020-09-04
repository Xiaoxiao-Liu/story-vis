from flask import Flask, render_template
import models as mode
from flask import request
from children_story_model.main_model import main_mod
from fenye import Fenye
from ci_fen import Word
from fenxi import Fenxi
from zishu import Wordxi
from dingwei import Dw
from flask_cors import CORS
from flask import  jsonify
import json
import re
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app, resources=r'/*')

title="狐狸和乌鸦的故事1"

@app.route('/', methods=['POST', 'GET'])
def main():
    # colors = []
    if request.method == 'GET':  # 网页一开始显示是“狐狸和乌鸦的故事”的分析内容
        # html_1='index2.html'

        title = "狐狸和乌鸦的故事"

    elif request.method == 'POST':
        all_title = request.form['crid']  # all_title接收用户的提交内容
        # a = request.form['form1']
        # print(a)
        titles = main_mod(all_title)  # titles获得推荐的故事题目
        title = titles[0]  # 因为titles是个列表，里面的故事题目有4个，就选取每次推荐的第一个，来进行可视化的展示
        print(title)  # title是最后展现的故事题目
        html_1 = 'index.html'
    else:
        pass
    try:
        # 接收title里面的故事题目做数值
        # dict1, dict2, dict3, dict4, title, Tcolors_2, Fcolors_2 = mode.data_for_vis(title, 1)

        dict1, dict2, dict3, dict4,  title, Tcolors, Fcolors = mode.data_for_vis(title)


    except ZeroDivisionError as e:  # 如果内容数据库里面没有会提示错误，并继续是最开始的主页故事
        print(e)
    # dict1, dict2, dict3, dict4, title, Tcolors, Fcolors = mode.data_for_vis("狐狸和乌鸦的故事")
    # html_1 = 'index2.html'
    # 情感词的页分页
    page = Fenye()
    fen_pages=page.qinggan(title,10)
    fenye_pages=[]
    for i in fen_pages.values():
        fenye_pages.append(i)
        #print(i)
    len_fen=len(fen_pages)
    # print(fenye_pages)
    #print(len_fen)

    #词性的页分页
    page_xi = Fenxi()
    fen_pages_xi = page_xi.cixing(title, 10)
    fenye_pages_xi_v = []
    for i in fen_pages_xi.values():
        fenye_pages_xi_v.append(i)
        # print(i)
    fenye_pages_xi_k = []
    for i in fen_pages_xi.keys():
        fenye_pages_xi_k.append(i)
    len_fen_xi_v = len(fenye_pages_xi_v)
    # print(fenye_pages_xi_v) #打印词性的值
    # print(fenye_pages_xi_k) #打印词性的键
    # print(len_fen_xi_v)

    pn_color,content,all_color,fcolor,tcolor,all_num,word, imgs, im_name, propertys, pro_name, pro_number, \
    pro_num, entropy_num, readability_num_1, readability_num_2, readability_num_3, readability_num_4, readability_num_5, \
    readability_num_6, readability_num_7, readability_num_8, readability_num_9, length_p = mode.models_mysql(
    title)
    count_dict = {}
    img_name = []
    for name in im_name:
        reg = name.split('.')[0]
        print("reg",reg)
        times = content.count(reg)
        print(times)
        count_dict[name] = times
    new_dict = sorted(count_dict.items(), key = lambda item:item[1], reverse=True)
    #print(new_dict)
    for ele in new_dict:
        img_name.append(ele[0])
    #print(img_name)


    return render_template('index.html', **locals())

#情感，用户选择分页数
@app.route('/fenye', methods=['POST'])
def post_Data():
    print(1)
    # 接收用户选择
    ye = request.form['ye']
    title = request.form['title']
    # print(ye)
    # print(title)
    # 调用分页类
    page = Fenye()
    # 调分页类的函数
    fen_pages= page.qinggan(title, int(ye))
    datas=[]
    # 将后台处理数据的值传到前端
    for data in fen_pages.values():
        datas.append(data)
    return json.dumps(datas, ensure_ascii=False)

#情感，用户选择分词数
@app.route('/fenci', methods=['POST'])
def post_Datas():
    print(2)
    # 接收用户选择
    zi = request.form['zi']
    title = request.form['title']
    # print(ye)
    # print(title)
    # 调用按字分页的类
    page = Word()
    # 这个类下面的函数
    fen_pages= page.ci_qinggan(title, int(zi))
    # all_num=page.num()
    # print(all)
    datas=[]
    # 接收处理数据,加载到前端
    for data in fen_pages.values():
        datas.append(data)

    return json.dumps(datas, ensure_ascii=False)


#词性，用户选择按照页分
@app.route('/fenxi', methods=['POST'])
def post_ci_Data():
    print(3)
    ye_xi = request.form['yexi']    #用户选择页数
    title = request.form['title']
    # print('ye_xi:',ye_xi)
    # print(title)
    # 调用词性里面的分页类
    page = Fenxi()
    # 调类的函数
    fen_pages_xi= page.cixing(title, int(ye_xi))
    data_v=[]
    # 接收后台处理数据,渲染到前端
    for i in fen_pages_xi.values():
        data_v.append(i)
        # print(i)
    return json.dumps(data_v, ensure_ascii=False)

#词性，用户按照字分
@app.route('/fenxizi', methods=['POST'])
def post_ci_Datas():
    print(4)
    # 用户选择按字分页数
    zi_xi = request.form['zixi']
    title = request.form['title']
    # print(ye)
    # print(title)
    # 调用按字分页的类
    page = Wordxi()
    # 类下的函数
    fen_pages_xi= page.cixing(title, int(zi_xi))
    # all_num=page.num()
    # print(all)
    datas_v=[]
    # 返回处理值,渲染到前端
    for data in fen_pages_xi.values():
        datas_v.append(data)

    return json.dumps(datas_v, ensure_ascii=False)

#词性用户搜索关键词
@app.route('/an', methods=['POST'])
def post_n():
    # 接收用户搜索的关键词内容
    all_n = request.form['searchg']
    # 获取现在分了多少页
    all_pages=request.form['all_page']
    title=request.form['title']
    # 调用关键词的类
    a = Dw()
    # 如果分页内容为空,则调用用户按照字分了多少页的数据
    if all_pages=="":
        all_pages = request.form['zi_page']
    #     接收后台数据返回前端
    return jsonify(a.ding_wei(title,int(all_pages),all_n))
if __name__ == '__main__':
    app.run()

