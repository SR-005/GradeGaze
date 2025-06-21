from flask import Flask, request, render_template

app=Flask(__name__)
@app.route("/")
def index():
    name,travel,study,failure,first,second=None
    if request.method=="POST":
        name=request.form.get["name"]
        travel=request.form.get["traveltime"]
        study=request.form.get["studytime"]
        failure=request.form.get["failure"]
        first=request.form.get["firstmark"]
        second=request.form.get["secondmark"]
    return render_template("index.html",name=name,travel=travel,study=study,failure=failure,first=first,second=second)

if __name__=="__main__":
    app.run(debug=True)