# 声明Netbook的类型，必须在引入pyecharts.charts等模块前声明
from pyecharts.globals import CurrentConfig,NotebookType
CurrentConfig.NOTBOOK_TYPE = NotebookType.JUPYTER_LAB

from pyecharts import options as opts
from pyecharts.charts import Calendar
import pymysql

# 连接MYSQUL数据库
conn = pymysql.connect ( host='127.0.0.1', port=3306, user='root', password="040521", db="sales", charset="utf8" )
cursor = conn.cursor()
sql_num = "SELECT trade_date,close FROM stocks WHERE year(trade_date)=2020"
cursor.execute(sql_num)
sh = cursor.fetchall ()
v1 = []
for s in sh:
    v1.append ( [s[0], s[1]] )
    data = v1


# 绘制日历图
def calendar_base() -> Calendar:
    c = (
        Calendar ()
        .add ( "", data, calendar_opts=opts.CalendarOpts ( range_="2020" ) )
        .set_global_opts (
            title_opts=opts.TitleOpts(title="2020年上半年股票收盘日历图"),
            visualmap_opts=opts.VisualMapOpts(
                max_=95,
                min_=65,
                orient="horizontal",  # vertical表示垂直的,horuzibtal表示水平的
                is_piecewise=True,
                pos_top="200px",
                pos_left="10px"
            ),
            toolbox_opts=opts.ToolboxOpts(is_show=False),
            legend_opts=opts.LegendOpts(is_show=True),
        )
    )
    return c


# # 第一次渲染时调用load_javascript文件
# calendar_base().load_javascript()
# # 展示数据可视化图标
# calendar_base().render_notebook()
calendar_base().render('123.html')