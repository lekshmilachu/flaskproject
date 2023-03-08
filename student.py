from flask import *
from database import DB,CR
from datetime import datetime

student = Blueprint("student",__name__)

@student.route("/")
def Studenthome():
    CR.execute("SELECT *FROM qanda")
    res = CR.fetchall()
    return render_template('studenthome.html',res=res)

@student.route("/examqn",methods = ["post",'get'])
def Examqn():
    CR.execute("SELECT * FROM qanda")
    res = CR.fetchall()

    if "submit" in request.form:
        question = request.form['ans']
        id = request.form["submit"]
        date = datetime.now()
        sql = 'UPDATE qanda set answer=%s, date=%s WHERE id=%s' 
        val = (question,date,id)
        CR.execute(sql,val)
        DB.commit()
        flash("Answer submitted")
        return redirect(url_for('student.Studenthome'))
        
    return render_template('examqn.html',res = res)


    