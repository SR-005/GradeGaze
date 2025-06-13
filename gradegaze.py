import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error

df=pd.read_csv("student-mat.csv")
dfmain=df.drop(["school","age","sex","address","famsize","Pstatus","Medu","Fedu","Mjob","Fjob","Fedu","reason","guardian","schoolsup","famsup","paid","activities","nursery","higher","famrel","freetime","goout","Dalc","Walc","health","absences","romantic","internet"],axis=1)
print(dfmain.info())

sns.pairplot(dfmain, kind="scatter",plot_kws={"alpha":0.5})
plt.show()
#features  are traveltime,studeytime,failures,G1,G2
#target variable is G3

#MODEL TRAINING 
#data setup

X=df[["traveltime","studytime","failures","G1","G2"]]
y=df["G3"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
lm=LinearRegression()
lm.fit(X_train,y_train)

prediction=lm.predict(X_test)
print(prediction)