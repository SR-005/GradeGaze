import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor,RandomForestClassifier
from sklearn.metrics import mean_absolute_error,mean_squared_error
import math

df=pd.read_csv("student-mat.csv")
dfmain=df.drop(["school","age","sex","address","famsize","Pstatus","Medu","Fedu","Mjob","Fjob","Fedu","reason","guardian","schoolsup","famsup","paid","activities","nursery","higher","famrel","freetime","goout","Dalc","Walc","health","absences","romantic","internet"],axis=1)
print(dfmain.info())

sns.pairplot(dfmain, kind="scatter",plot_kws={"alpha":0.5})
'''plt.show()'''
#features  are traveltime,studeytime,failures,G1,G2
#target variable is G3

#setup new column for grades
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
    
df["grades"]=df["G3"].apply(markgrades)
print(df.head(10))
#MODEL TRAINING 
#data setup
X=df[["traveltime","studytime","failures","G1","G2"]]
ymark=df["G3"]
ygrade=df["grades"]


X_train,X_test,ymark_train,ymark_test,ygrade_train,ygrade_test=train_test_split(X,ymark,test_size=0.2,random_state=42)
#LINEAR REGRESSION
'''lm=LinearRegression()
lm.fit(X_train,y_train)
prediction=lm.predict(X_test)'''

#RandomForest Regression
rfr=RandomForestRegressor(n_estimators=100,random_state=42)
rfr.fit(X_train,ymark_train)
prediction=rfr.predict(X_test)

#RandomForest Classifier
rfc=RandomForestClassifier(n_estimators=100,random_state=42)
rfc.fit(X_train,ygrade_train)
prediction2=rfc.predict(X_test)

'''print(prediction)'''
#REGRESSION ERROR
er1=mean_absolute_error(ymark_test,prediction)
er2=mean_squared_error(ymark_test,prediction)
er3=math.sqrt(er2)

print("Mean Absolute Error: ",er1)
print("Mean Squared Error:",er2)
print("Root Mean Squared Error: ",er3)
