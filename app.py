from flask import Flask, request, render_template
import joblib
import pandas as pd

app=Flask(__name__)
@app.route("/",methods=["GET", "POST"])
def index():
    name=None
    data=None
    mark=None
    grade=None
    G1=None
    G2=None
    if request.method=="POST":
        name=request.form.get("name")
        data={"traveltime":int(request.form.get("traveltime")),
          "studytime":int(request.form.get("studytime")),
          "failures":int(request.form.get("failures")),
          "G1":int(request.form.get("firstmark")),
          "G2":int(request.form.get("secondmark"))}
        print(data)

        #machine learning prediction
        xgb=joblib.load("xgb.pkl")  #loading the model
        inputdf=pd.DataFrame([data])   #setting data for pandas
        prediction=xgb.predict(inputdf)[0]  

        def markgrades(mark):
            if mark>=16:
                return "A"
            elif mark>=14:
                return "B"
            elif mark>=12:
                return "C"
            elif mark>=10:
                return "D"
            else:
                return "F"
            
        #Rounding off marks for better viewer accuracy
        mark=round(prediction)
        grade=markgrades(mark)
        G1=int(request.form.get("firstmark"))
        G2=int(request.form.get("secondmark"))
        print("Mark:",mark,"\nGrade:",grade)
    return render_template("index.html",mark=mark,grade=grade,name=name,G1=G1,G2=G2)

if __name__=="__main__":
    app.run(debug=True)