import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


df=pd.read_csv("student-mat.csv")
dfdup=df.drop(["school","age","sex","address","famsize","Pstatus","Medu","Fedu","Mjob","Fjob","Fedu","reason","guardian","schoolsup","famsup","paid","activities","nursery","higher","famrel","freetime","goout","Dalc","Walc","health","absences","romantic"],axis=1)
print(dfdup.info())