from flask import *
from database import DB,CR
from datetime import datetime

teacher = Blueprint("teacher",__name__)


@teacher.route("/")
def Teacherhome():
    return render_template('teacherhome.html')

@teacher.route("/examans",methods = ["post",'get'])
def Examans():
    CR.execute("SELECT * FROM qanda")
    qanda =  CR.fetchall()
    if "submit" in request.form:
        question = request.form["question"]
        sql =  "INSERT INTO qanda (question,answer,date) VALUES (%s,%s,%s)"
        val = (question,"",datetime.now())
        CR.execute(sql,val)
        DB.commit()
        return render_template('examans.html',qanda = qanda)

    return render_template('examans.html',qanda = qanda)

@teacher.route("/examres")
def Examres():
    CR.execute('SELECT *FROM qanda')
    res = CR.fetchall()
    
    return render_template('examres.html',res=res)
    