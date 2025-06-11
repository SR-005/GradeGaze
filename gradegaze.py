import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


df=pd.read_csv("student-mat.csv")
dfdup=df.drop(["school","sex","address","famsize","Pstatus","Medu","Fedu","Mjob","Fedu","reason","guardian","schoolsup","famsup","paid","activities","nursery","higher","famrel","freetime","goout","Dalc","Walc","health","absences"],axis=1)
print(dfdup.info())