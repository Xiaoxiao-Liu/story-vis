//左一是放的角色所以没有js内容
//左二放的是摘要没有可视化
//左三可视化
(function () {
    //基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.querySelector(".pie .chart"));
// 指定图表的配置项和数据
    option = {
    tooltip: {
        trigger: 'axis',
        // 坐标轴指示器，坐标轴触发有效
        axisPointer: {
             // 默认为直线，可选为：'line' | 'shadow'
            type: 'shadow'
        }
    },
    //    直角坐标系内绘图网格
    grid: {
        //图例组件离容器左侧的距离
        left: '3%',
        //图例组件离容器右侧的距离
        right: '4%',
        //图例组件离容器下侧的距离
        bottom: '3%',
        //是否含坐标轴的刻度标签
        containLabel: true
    },
    //    x轴设置
    xAxis: {
        //坐标轴的类型：value是连续数据
        type: 'value'
    },
        //    y轴设置
    yAxis: {
        //坐标轴的类型：category是类目轴，适用于离散的类目数据
        //该类型必须通过data设置类目数据
        type: 'category',
        data: ['公式一', '公式二', '公式三', '公式四']
    },



    //    系列列表
    series: [
        {
            name: '文本难字率',
            //图的类型，bar是条形图，line是直线图，pie是饼图
            type: 'bar',
            //数据堆积
            stack: '总量',
            label: {
                //是否显示提示框组件，包括提示框浮层
                show: true,
                //标签的位置
                position: 'insideRight'
            },
            //readability_1为文本难字率的值
            //数据已经按照data规律写好放在index.html的js里，所以可以直接调取
            color:'#4695d6',
            data: readability_1
        },
        {
            name:  '平均笔画数',
            //图的类型，bar是条形图，line是直线图，pie是饼图
            type: 'bar',
            //数据堆积
            stack: '总量',
            label: {
                //是否显示提示框组件，包括提示框浮层
                show: true,
                //标签的位置
                position: 'insideRight'
            },
            //readability_2为平均笔画数的值
            //数据已经按照data规律写好放在index.html的js里，所以可以直接调取

            color:'#fdc300',
            data:readability_2
        },
        {
            name: '文本总词数',
            //图的类型，bar是条形图，line是直线图，pie是饼图
            type: 'bar',
            //数据堆积
            stack: '总量',
            label: {
                //是否显示提示框组件，包括提示框浮层
                show: true,
                //标签的位置
                position: 'insideRight'
            },
            //readability_3为文本总词数值
            //数据已经按照data规律写好放在index.html的js里，所以可以直接调取

            color:"#fa6e57",
            data: readability_3
        },
        {
            //图的类型，bar是条形图，line是直线图，pie是饼图
            type: 'bar',
            //数据堆积
            stack: '总量',
            label: {
                //是否显示提示框组件，包括提示框浮层
                show: true,
                //标签的位置
                position: 'insideRight'
            },
            //readability_4为总句子数
            //数据已经按照data规律写好放在index.html的js里，所以可以直接调取

            color:"#739e3b",
            data: readability_4
        },
        {
            name: '熟悉词数量',
            //图的类型，bar是条形图，line是直线图，pie是饼图
            type: 'bar',
            //数据堆积
            stack: '总量',
            label: {
                //是否显示提示框组件，包括提示框浮层
                show: true,
                //标签的位置
                position: 'insideRight'
            },
            //readability_5为熟悉词数量
            //数据已经按照data规律写好放在index.html的js里，所以可以直接调取

            color:"#DADDD8",
            data: readability_5
        },
        {
            name: '平均每句字数',
            //图的类型，bar是条形图，line是直线图，pie是饼图
            type: 'bar',
            //数据堆积
            stack: '总量',
            label: {
                //是否显示提示框组件，包括提示框浮层
                show: true,
                //标签的位置
                position: 'insideRight'
            },
            //readability_6为平均每句字数
            //数据已经按照data规律写好放在index.html的js里，所以可以直接调取

            color:"#e8a0b8",
            data: readability_6
        },
        {
            name: '完整句子比率',
            //图的类型，bar是条形图，line是直线图，pie是饼图
            type: 'bar',
            //数据堆积
            stack: '总量',
            label: {
                //是否显示提示框组件，包括提示框浮层
                show: true,
                //标签的位置
                position: 'insideRight'
            },
            //readability_7完整句子比率
            //数据已经按照data规律写好放在index.html的js里，所以可以直接调取

            color:"#a5dff9",
            data: readability_7
        },
        {
            name: '每句平均词数',
            //图的类型，bar是条形图，line是直线图，pie是饼图
            type: 'bar',
            //数据堆积
            stack: '总量',
            label: {
                //是否显示提示框组件，包括提示框浮层
                show: true,
                //标签的位置
                position: 'insideRight'
            },
            //readability_8为每句平均词数
            //数据已经按照data规律写好放在index.html的js里，所以可以直接调取

            color:"#f5962a",
            data: readability_8
        },
        {
            name: '文本难词数',
            //图的类型，bar是条形图，line是直线图，pie是饼图
            type: 'bar',
            //数据堆积
            stack: '总量',
            label: {
                //是否显示提示框组件，包括提示框浮层
                show: true,
                //标签的位置
                position: 'insideRight'
            },
            //readability_9为文本难词数
            //数据已经按照data规律写好放在index.html的js里，所以可以直接调取

            color:"#01a9d0",
            data: readability_9
        }
    ]
};
    //使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    // 让图表跟随屏幕自动的去适应
    window.addEventListener("resize", function () {
        myChart.resize();
    });
})();

// 右一可视化
(function () {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.querySelector(".bar2 .chart"));
    // 指定图表的数据
    var data = [
        {
        name: ' ',
        //正面词性区域的颜色
        itemStyle: {
            color: '#E684AE'
        },
        //di_1是正面词跟颜色
        children: di_1
    },
        {
        name: ' ',
        //负面词性区域的颜色
        itemStyle: {
            color: '#77A1D3'
        },
        //di_2是负面词跟颜色
        children: di_2
    }];
    // 指定图表的配置项
    var option = {
        // title: {
        //     text: '文本词汇情感分析',
        //     //文本内容设置
        //     textStyle: {
        //         fontSize: 24,
        //         //位置靠左方
        //         align: 'left'
        //     },
        // },
        //系列列表。每个系列通过 type 决定自己的图表类型
        series: {
            center: ['50%', '40%'],
            //图表类型为旭日图
            type: 'sunburst',
            //当鼠标悬停不相关扇形块的配置
            highlightPolicy: 'ancestor',
            data: data,
            //圆角半径
            //radius: [0, '95%'],
            //扇形根据数据value的排序方式，desc为降序排序，asc为升序排序，null为不排序
            sort: null,
            //对层的配置
            levels: [{}, {
                //第一层的圆心角度
                r0: '1%',
                r: '3%',
                //这块的设置
                itemStyle: {
                    //边框线宽
                    borderWidth: 2
                },
                label: {
                    //标签旋转。从 -90 度到 90 度。正值是逆时针。
                    rotate: 'tangential'
                }
            }, {
                //第二层的圆心角度
                r0: '3%',
                r: '25%',
                label: {
                    //标签位置靠右
                    align: 'right'
                }
            }, {
                //第三层的圆心角度
                r0: '25%',
                r: '27%',
                label: {
                    position: 'outside',
                    // padding: 3,
                    //是否静态无法交互
                    silent: false
                },
                itemStyle: {
                    borderWidth: 3
                }
            }]
        }
    };

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
//让图表跟随屏幕自动的去适应
    window.addEventListener("resize", function () {
        myChart.resize();
    });
})();

//右二可视化
(function () {
// 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.querySelector(".line2 .chart"));
    // 指定图表的配置项和数据
    option = {

        //提示框组件
        tooltip: {},
        //雷达图的坐标系组件
        radar: {
            name: {
                //字体设置
                textStyle: {
                    color: '#fff',
                    backgroundColor: '#999',
                    //富文本标签
                    borderRadius: 1,
                    //文字块的内边距[上，右，下，左]
                    padding: [1, 2]
                }
            },
            //雷达图的指示器，用来指定雷达图中的多个维度
            indicator: [
                {name: '情感度信息熵', max: 1},
                {name: '词性信息熵', max: 1},
                //重要性信息熵这个维度
                {name: '重要性信息熵', max: 1},
                {name: '笔画数信息熵', max: 1},
                {name: '笔画大于16的笔画', max: 0.12},
            ],
            center: ['50%', '60%'],
             splitArea: {
                areaStyle: {
                    color: ['rgba(114, 172, 209, 0.2)',
                        'rgba(114, 172, 209, 0.4)', 'rgba(114, 172, 209, 0.6)',
                        'rgba(114, 172, 209, 0.8)', 'rgba(114, 172, 209, 1)'],
                    shadowColor: 'rgba(0, 0, 0, 0.3)',
                    shadowBlur: 10
                }
            },
        },
        //整体数据设置
        series: [
            {
            type: 'radar',
            //提示框组件
            tooltip: {
                //触发类型： item数据项图形触发，主要在散点图，饼图等无类目轴的图表中使用。
                //触发类型： axis坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用。
                //触发类型： none是什么也不触发
                trigger: 'item'
            },
            //展现变化趋势
            areaStyle: {},
            data: [
                {
                    //数据库调数据
                    value: data_entropy,
                },
            ]
        }]
    };
    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
//让图表跟随屏幕自动的去适应
    window.addEventListener("resize", function () {
        myChart.resize();
    });
})();

//右三可视化
(function () {
    //基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.querySelector(".pie2 .chart"));
    //指定图表的配置项和数据
    var option = {
        color: data_color,
        //提示框组件
        tooltip: {
            trigger: "item",
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        //整体数据设置
        series: [
            {
                name: "词性分布",
                //图类型饼图
                type: "pie",
                radius: ["2%", "70%"],
                center: ["50%", "40%"],
                //扇区圆心角展现数据的百分比
                roseType: "radius",
                // 图形的文字标签
                label: {
                    fontSize: 7
                },
                // 链接图形和文字的线条
                labelLine: {
                    // length 链接图形的线条
                    length: 1,
                    // length2 链接文字的线条
                    length2: 0.1
                },
                //调的数据库里面数据
                data: data_pro
            }
        ],
    };
    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    // 监听浏览器缩放，图表对象调用缩放resize函数
    window.addEventListener("resize", function () {
        myChart.resize();
    });
})();
//左一没有浮窗的echarts可视化
//左二没有浮窗的echarts可视化
//左三的浮窗可视化
(function () {
    //基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('login5'));// 指定图表的配置项和数据
        option = {
            legend: {
                data: [ '文本难字率','平均笔画数','文本总词数','熟悉词数量','平均每句字数','完整句子比率', '每句平均词数', '文本难词数',],
                top: 20,
                left: 10,
                orient: 'vertical',
                itemGap: 0,
                icon: 'rect',
            },
    tooltip: {
        trigger: 'axis',
        // 坐标轴指示器，坐标轴触发有效
        axisPointer: {
             // 默认为直线，可选为：'line' | 'shadow'
            type: 'shadow'
        }
    },
    //    直角坐标系内绘图网格
    grid: {
        //图例组件离容器左侧的距离
        left: '10%',
        //图例组件离容器右侧的距离
        right: '4%',
        //图例组件离容器下侧的距离
        bottom: '3%',
        //是否含坐标轴的刻度标签
        containLabel: true
    },
    //    x轴设置
    xAxis: {
        //坐标轴的类型：value是连续数据
        type: 'value'
    },
        //    y轴设置
    yAxis: {
        //坐标轴的类型：category是类目轴，适用于离散的类目数据
        //该类型必须通过data设置类目数据
        type: 'category',
        data: ['公式一', '公式二', '公式三', '公式四']
    },
    //    系列列表
    series: [
        {
            name: '文本难字率',
            //图的类型，bar是条形图，line是直线图，pie是饼图
            type: 'bar',
            //数据堆积
            stack: '总量',
            label: {
                //是否显示提示框组件，包括提示框浮层
                show: true,
                //标签的位置
                position: 'insideRight'
            },
            //readability_1为文本难字率的值
            //数据已经按照data规律写好放在index.html的js里，所以可以直接调取
            color:'#4695d6',

            data: readability_1
        },
        {
            name:  '平均笔画数',
            //图的类型，bar是条形图，line是直线图，pie是饼图
            type: 'bar',
            //数据堆积
            stack: '总量',
            label: {
                //是否显示提示框组件，包括提示框浮层
                show: true,
                //标签的位置
                position: 'insideRight'
            },
            //readability_2为平均笔画数的值
            //数据已经按照data规律写好放在index.html的js里，所以可以直接调取
            color:'#fdc300',

            data:readability_2
        },
        {
            name: '文本总词数',
            //图的类型，bar是条形图，line是直线图，pie是饼图
            type: 'bar',
            //数据堆积
            stack: '总量',
            label: {
                //是否显示提示框组件，包括提示框浮层
                show: true,
                //标签的位置
                position: 'insideRight'
            },
            //readability_3为文本总词数值
            //数据已经按照data规律写好放在index.html的js里，所以可以直接调取
            color:"#fa6e57",

            data: readability_3
        },
        {
            //图的类型，bar是条形图，line是直线图，pie是饼图
            type: 'bar',
            //数据堆积
            stack: '总量',
            label: {
                //是否显示提示框组件，包括提示框浮层
                show: true,
                //标签的位置
                position: 'insideRight'
            },
            //readability_4为总句子数
            //数据已经按照data规律写好放在index.html的js里，所以可以直接调取
            color:"#739e3b",

            data: readability_4
        },
        {
            name: '熟悉词数量',
            //图的类型，bar是条形图，line是直线图，pie是饼图
            type: 'bar',
            //数据堆积
            stack: '总量',
            label: {
                //是否显示提示框组件，包括提示框浮层
                show: true,
                //标签的位置
                position: 'insideRight'
            },
            //readability_5为熟悉词数量
            //数据已经按照data规律写好放在index.html的js里，所以可以直接调取
            color:"#DADDD8",

            data: readability_5
        },
        {
            name: '平均每句字数',
            //图的类型，bar是条形图，line是直线图，pie是饼图
            type: 'bar',
            //数据堆积
            stack: '总量',
            label: {
                //是否显示提示框组件，包括提示框浮层
                show: true,
                //标签的位置
                position: 'insideRight'
            },
            //readability_6为平均每句字数
            //数据已经按照data规律写好放在index.html的js里，所以可以直接调取
            color:"#e8a0b8",

            data: readability_6
        },
        {
            name: '完整句子比率',
            //图的类型，bar是条形图，line是直线图，pie是饼图
            type: 'bar',
            //数据堆积
            stack: '总量',
            label: {
                //是否显示提示框组件，包括提示框浮层
                show: true,
                //标签的位置
                position: 'insideRight'
            },
            //readability_7完整句子比率
            //数据已经按照data规律写好放在index.html的js里，所以可以直接调取
            color:"#a5dff9",

            data: readability_7
        },
        {
            name: '每句平均词数',
            //图的类型，bar是条形图，line是直线图，pie是饼图
            type: 'bar',
            //数据堆积
            stack: '总量',
            label: {
                //是否显示提示框组件，包括提示框浮层
                show: true,
                //标签的位置
                position: 'insideRight'
            },
            //readability_8为每句平均词数
            //数据已经按照data规律写好放在index.html的js里，所以可以直接调取
            color:"#f5962a",

            data: readability_8
        },
        {
            name: '文本难词数',
            //图的类型，bar是条形图，line是直线图，pie是饼图
            type: 'bar',
            //数据堆积
            stack: '总量',
            label: {
                //是否显示提示框组件，包括提示框浮层
                show: true,
                //标签的位置
                position: 'insideRight'
            },
            //readability_9为文本难词数
            //数据已经按照data规律写好放在index.html的js里，所以可以直接调取
            color:"#01a9d0",
            data: readability_9
        }
    ]
};
    //使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    // 让图表跟随屏幕自动的去适应
    window.addEventListener("resize", function () {
        myChart.resize();
    });
})();

// 右一的浮窗可视化
//
(function () {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('login2'));
    var xAxisData = [];
    //放入甜甜圈数据
    var data = [
        {
        name: '正面词性',
        //正面词性区域的颜色
        itemStyle: {
            color: '#E684AE'
        },
        //di_1是正面词跟颜色
        children: di_1
    },
        {
        name: '负面词性',
        //负面词性区域的颜色
        itemStyle: {
            color: '#77A1D3'
        },
        //di_2是负面词跟颜色
        children: di_2
    }];
    // 指定图表的数据

//加入初始页数
for (var i = 1; i < 11; i++) {
    xAxisData.push('Page' + i);
}
//设置可视化
option = {
    //可视化背景
    backgroundColor: '#eee',
    //可视化的图例设置
    legend: {
        data: ['赞扬', '快乐', '尊敬', '喜爱', '相信', '惊奇',
                        '思念', '安心', '祝愿','贬责', '烦闷', '憎恶',
                        '悲伤', '恐惧', '内疚', '慌张', '失望', '害羞',
                        '妒忌','怀疑'],
        //图例位置
        left: 10,
        //图例为长方形
        orient: 'vertical',
        //两两图例之间距离为0
        itemGap:0,
        icon: 'rect',
    },

    //x轴设计
    xAxis: {
        data:xAxisData,
        name: '页数',
        //是否x轴从0开始
        axisLine: {onZero: true},
        //是否加辅助线
        splitLine: {show: false},
        splitArea: {show: false}
    },
    //y轴设计
    yAxis: {
        // inverse: true,
        //是否加辅助线
        splitArea: {show: false}
    },
    //条形图的大小
    grid: {
         right:'35%',
        bottom: 100,
    },
    //条形图的数据
    series: [
        {center: ['84%', '25%'],
            //图表类型为旭日图
            type: 'sunburst',
            //当鼠标悬停不相关扇形块的配置
            highlightPolicy: 'ancestor',
            data: data,
            //圆角半径
            //radius: [0, '95%'],
            //扇形根据数据value的排序方式，desc为降序排序，asc为升序排序，null为不排序
            sort: null,
            //对层的配置
            levels: [{}, {
                //第一层的圆心角度
                r0: '1%',
                r: '10%',
                //这块的设置
                itemStyle: {
                    //边框线宽
                    borderWidth: 2
                },
                label: {
                    //标签旋转。从 -90 度到 90 度。正值是逆时针。
                    rotate: 'tangential'
                }
            }, {
                //第二层的圆心角度
                r0: '10%',
                r: '25%',
                label: {
                    //标签位置靠右
                    align: 'right'
                }
            }, {
                //第三层的圆心角度
                r0: '25%',
                r: '27%',
                label: {
                    position: 'outside',
                    padding: 3,
                    //是否静态无法交互
                    silent: false
                },
                //字体样式
                itemStyle: {
                    borderWidth: 3
                }
            }]},
          //以下都为条形图的数据结构
          {
            name: '赞扬',
            type: 'bar',
            stack: 'one',
            data: fenye[0],
            color:fc[3],
        },
        {
            name: '快乐',
            type: 'bar',
            stack: 'one',
            data: fenye[1],
            color:fc[4],
        },
        {
            name: '尊敬',
            type: 'bar',
            stack: 'one',
            data: fenye[2],
            color:fc[7],
        },
        {
            name: '喜爱',
            type: 'bar',
            stack: 'one',
            data: fenye[3],
            color:fc[5],
        },
        {
            name: '相信',
            type: 'bar',
            stack: 'one',
            data: fenye[4],
            color:fc[11],
        },
         {
            name: '惊奇',
            type: 'bar',
            stack: 'one',
            data: fenye[5],
             color:fc[12],
        },
         {
            name: '思念',
            type: 'bar',
            stack: 'one',
            data: fenye[6],
             color:fc[10],
        },
         {
            name: '安心',
            type: 'bar',
            stack: 'one',
            data: fenye[7],
             color:fc[6],
        },
         {
            name: '祝愿',
            type: 'bar',
            stack: 'one',
            data: fenye[8],
             color:fc[8],
        },
         {
            name: '贬责',
            type: 'bar',
            stack: 'one',
            data: fenye[9],
             color:fc[1],
        },
         {
            name: '烦闷',
            type: 'bar',
            stack: 'one',
            data: fenye[10],
             color:fc[2],
        },
         {
            name: '憎恶',
            type: 'bar',
            stack: 'one',
            data: fenye[11],
             color:fc[18],
        },
         {
            name: '悲伤',
            type: 'bar',
            stack: 'one',
            data: fenye[12],
             color:fc[0],
        },
         {
            name: '恐惧',
            type: 'bar',
            stack: 'one',
            data: fenye[13],
             color:fc[16],
        },
         {
            name: '内疚',
            type: 'bar',
            stack: 'one',
            data: fenye[14],
             color:fc[14],
        },
         {
            name: '慌张',
            type: 'bar',
            stack: 'one',
            data: fenye[15],
             color:fc[15],
        },
         {
            name: '失望',
            type: 'bar',
            stack: 'one',
            data: fenye[16],
             color:fc[13],
        },
         {
            name: '害羞',
            type: 'bar',
            stack: 'one',
            data: fenye[17],
             color:fc[17],
        },
         {
            name: '妒忌',
            type: 'bar',
            stack: 'one',
            data: fenye[18],
             color:fc[19],
        },
         {
            name: '怀疑',
            type: 'bar',
            stack: 'one',
            data: fenye[19],
             color:fc[9],
        },
    ]
};

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
//让图表跟随屏幕自动的去适应
    window.addEventListener("resize", function () {
        myChart.resize();
    });
})();
// 右二的浮窗可视化
(function () {
// 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('login4'));
    // 指定图表的配置项和数据
    option = {
        title: {
            text: '信息熵雷达图'
        },
        //提示框组件
         tooltip: {},
        radar: {
            name: {
                //字体设置
                textStyle: {
                    color: '#fff',
                    backgroundColor: '#999',
                    //富文本标签
                    borderRadius: 3,
                    //字体块内部间距[上，右，下，左]
                    padding: [3, 5]
                }
            },
            //雷达图的指示器，用来指定雷达图中的多个维度
            indicator: [
                {name: '情感度信息熵', max: 1},
                {name: '词性信息熵', max: 1},
                //重要性信息熵这个维度
                {name: '重要性信息熵', max: 1},
                {name: '笔画数信息熵', max: 1},
                {name: '笔画大于16的笔画', max: 0.12},
            ],
             splitArea: {
                areaStyle: {
                    color: ['rgba(255,228,181, 0.2)',
                        'rgba(255,228,181, 0.4)', 'rgba(255,228,181, 0.6)',
                        'rgba(255,228,181, 0.8)', 'rgba(255,228,181, 1)'],
                    shadowColor: 'rgba(0, 0, 0, 0.3)',
                    shadowBlur: 10
                }
            },
        },
        //整体数据设置
        series: [{
            type: 'radar',
            //提示框组件
            tooltip: {
                //触发类型： item数据项图形触发，主要在散点图，饼图等无类目轴的图表中使用。
                //触发类型： axis坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用。
                //触发类型： none是什么也不触发
                trigger: 'item'
            },
            //展现变化趋势
            areaStyle: {},
            data: [
                {
                    //data_entropy=[情感度信息熵,词性信息熵,重要性信息熵,笔画数信息熵,笔画大于16的笔画]
                    value: data_entropy,
                },
            ]
        }]
    };
    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
//让图表跟随屏幕自动的去适应
    window.addEventListener("resize", function () {
        myChart.resize();
    });
})();

//右三的浮窗可视化
(function () {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('login6'));
    // 指定图表的数据
    var xAxisData=[]
//    可视化初始页数，也就是初始条数
for (var i = 1; i < 11; i++) {
    xAxisData.push('Page' + i);
}
    // 指定图表的配置项和数据
    option = {
    //后台传进来的颜色
    color: data_color,
    backgroundColor: '#eee',
    //    可视化的图例设置
    legend: {
        //后台传进来的图例名字
        data: length_name,
        left: 0.1,
        //设计图例为长方形
        orient: 'vertical',
        //两辆图例之间间隔为0
        itemGap:0,
        icon: 'rect',
    },
    //对于x轴的设计
    xAxis: {
        data: xAxisData,
        name: '页数',
        //x轴从0开始
        axisLine: {onZero: true},
        //x轴是否添加辅助线
        splitLine: {show: false},
        splitArea: {show: false}
    },
    //    y轴设计
    yAxis: {
        // inverse: true,
        //x轴是否添加辅助线
        splitArea: {show: false}
    },
    //    整体条形图的大小设计
    grid: {
         right:'40%',
        bottom: 100,
    },
    //后台传进来的数据
    series: pronames,
};
    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    // 监听浏览器缩放，图表对象调用缩放resize函数
    window.addEventListener("resize", function () {
        myChart.resize();
    });
})
();

// var button_names =
// $(button).click = function () {
//             //alert($("#this_role")[0].src);
//
//             console.log($("#this_role")[0].src)
//             console.log())
//         };
//浮窗的函数
(function () {
    function $(id) {


        return typeof id === "string" ? document.getElementById(id) : null;

    }

    //点击事件
    window.onload = function () {



        $('b1').onclick = function () {
            //显示面板和蒙版
            $('log1').style.display = 'block';
            $('login1').style.display = 'block';

            //隐藏滚动条
            document.body.style.overflow = 'hidden';
        };
        $('log1').onclick = function () {
            //隐藏面板和蒙版
            $('log1').style.display = 'none';
            $('login1').style.display = 'none';
        };

        $('b2').onclick = function () {
            //显示面板和蒙版
            $('log2').style.display = 'block';
            $('login2wear').style.display = 'block';
            document.getElementsByClassName("login2top")[0].style.display = 'block';
            //隐藏滚动条
            document.body.style.overflow = 'hidden';
        };
        //当点到的id=log2的时候
        $('log2').onclick = function () {
            //隐藏面板和蒙版
            $('log2').style.display = 'none';
            $('login2wear').style.display = 'none';
            document.getElementsByClassName("login2top")[0].style.display = 'none';
        };
        $('l1').onclick = function () {
            //显示面板和蒙版
            $('log3').style.display = 'block';
            $('login3').style.display = 'block';
            //隐藏滚动条
            document.body.style.overflow = 'hidden';
            // console.log('Worked')
        };
        $('log3').onclick = function () {
            //隐藏面板和蒙版
            $('log3').style.display = 'none';
            $('login3').style.display = 'none';
        };
        $('l2').onclick = function () {
            //显示面板和蒙版
            $('log4').style.display = 'block';
            $('login4').style.display = 'block';
            //隐藏滚动条
            document.body.style.overflow = 'hidden';
        };
        $('log4').onclick = function () {
            //隐藏面板和蒙版
            $('log4').style.display = 'none';
            $('login4').style.display = 'none';
        };
        $('p1').onclick = function () {
            //显示面板和蒙版
            $('log5').style.display = 'block';
            $('login5').style.display = 'block';
            //隐藏滚动条
            document.body.style.overflow = 'hidden';
        };
        $('log5').onclick = function () {
            //隐藏面板和蒙版
            $('log5').style.display = 'none';
            $('login5').style.display = 'none';
        };
        $('p2').onclick = function () {
            //显示面板和蒙版
            $('log6').style.display = 'block';
            $('login6').style.display = 'block';
            $("login6wear").style.display='block'
            //隐藏滚动条
            document.body.style.overflow = 'hidden';
        };
        $('log6').onclick = function () {
            //隐藏面板和蒙版
            $('log6').style.display = 'none';
            $('login6').style.display = 'none';
            $("login6wear").style.display='none'
            gldata=""
        };
    };

})();
