import math
import pandas as pd
import plotly.express as px
df = pd.read_csv('class2.csv')
marks = df['Marks'].tolist()
n = len(marks)
sum=0
for m in marks:
    sum = sum+m
mean = sum/n
sum=0
for m in marks:
    s = m - mean
    sq = s*s
    sum = sum + sq
result = math.sqrt(sum/(n-1))
print(result)


