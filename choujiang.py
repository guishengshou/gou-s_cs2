#让电脑支持访问服务
#需要一个框架web
# pip install Flask
from flask import Flask,render_template#导入
from random import randint
app = Flask(__name__,template_folder='templates')

shouqiang = ['P2000','USP','Glock','DualBerettas','P250','Fiveseven','Tec-9','CZ75','DesertEagle','R8 左轮',]
duanqiang = ['MP9','MAC-10','MP7','UMP45','P90','PP-Bizon','Nova','Xm1014','MAG-7','Sawed-Off','M249','Negev']
changqiang = ['SSG 08','AWP','SCAR-20','G3SG1','Famas','Galil AR','M4A4','M4A1 Silencer','AK-47','AUG','SG 553']
@app.route('/index')
def index():
    return render_template('index.html',shouqiang=shouqiang,duanqiang=duanqiang,changqiang=changqiang)
@app.route('/shouqiang1')

def shouqiang1():
    num0 = randint(0, len(shouqiang) - 1)
    return render_template('index.html', shouqiang=shouqiang, duanqiang=duanqiang, changqiang=changqiang,h_shouqiang=shouqiang[num0])#,h_duanqiang=duanqiang[num1], h_changqiang=changqiang[num2])
@app.route('/duanqiang1')
def duanqiang1() :
    num1 = randint(0, len(duanqiang) - 1)
    return render_template('index.html', shouqiang=shouqiang, duanqiang=duanqiang, changqiang=changqiang, h_duanqiang=duanqiang[num1])
@app.route('/changqiang1')
def changqiang1() :
    num2 = randint(0, len(changqiang) - 1)
    return render_template('index.html', shouqiang=shouqiang, duanqiang=duanqiang, changqiang=changqiang,h_changqiang=changqiang[num2])
app.run(debug=True)

