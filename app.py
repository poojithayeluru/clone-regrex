
from flask import Flask,request,render_template
import re
app=Flask(__name__)


@app.route("/")
def hi_page():
    return render_template("dispaly.html")
@app.route("/")
def home():
    if request.method=="post":
        Enter_a_text=request.form["inpu1"]
        Expression=request.form["inpu2"]
        matches=re.findall(Expression,Enter_a_text)
        count=len(matches)
        return render_template("result.html", count=count,matches=matches)
    else:
        return render_template("dispaly.html")  

@app.route("/",methods=['GET','POST'])
def h():
    Enter_a_text=request.form["inpu1"]
    Expression=request.form["inpu2"]
    matches=re.findall(Expression,Enter_a_text)
    count=len(matches)
    return render_template("result.html", count=count,matches=matches)
       

if __name__=="__main__":
    app.run(debug=True)