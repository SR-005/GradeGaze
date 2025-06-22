from flask import Flask, request, render_template
from gradegaze import markprediction as markp

app=Flask(__name__)
@app.route("/",methods=["GET", "POST"])
def index():
    name=None
    global data
    data=None
    mark=None
    grade=None
    if request.method=="POST":
        name=request.form.get("name")
        data={"traveltime":int(request.form.get("traveltime")),
          "studytime":int(request.form.get("studytime")),
          "failures":int(request.form.get("failures")),
          "G1":int(request.form.get("firstmark")),
          "G2":int(request.form.get("secondmark"))}
    print(data)
    mark,grade=markp(data)
    print(mark,"    ",grade)
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)