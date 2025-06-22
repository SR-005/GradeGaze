from flask import Flask, request, render_template
from gradegaze import markprediction as markp

app=Flask(__name__)
@app.route("/",methods=["GET", "POST"])
def index():
    name=None
    travel=None
    study=None
    failure=None
    first=None
    second=None
    mark=None
    grade=None
    if request.method=="POST":
        name=request.form.get("name")
        travel=request.form.get("traveltime")
        study=request.form.get("studytime")
        failure=request.form.get("failure")
        first=request.form.get("firstmark")
        second=request.form.get("secondmark")
    data={int(travel),int(study),int(failure),int(first),int(second)}
    print(name," ",travel," ",study," ",failure," ",first," ",second," ")
    mark,grade=markp(travel,study,failure,first,second)
    print(mark,"    ",grade)
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)