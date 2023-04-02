import pandas as pd
import statistics as s
import plotly.figure_factory as ff
import csv
import random


m_final=[]
list1_std=[]
list2_std=[]
list3_std=[]

df=pd.read_csv("StudentsPerformance.csv")
m_final=df["reading score"].tolist()

mean=sum(m_final)/len(m_final)
print("mean:",mean)

median=s.median(m_final)
print("median:",median)

mode=s.mode(m_final)
print("mode:",mode)

std=s.stdev(m_final)
print("standard deviation:",std)

one_std_start,one_std_end=mean-std,mean+std
two_std_start,two_std_end=mean-2*std,mean+2*std
third_std_start,third_std_end=mean-3*std,mean+3*std

for a in m_final :
    if a>one_std_start and a<one_std_end:
        list1_std.append(a)

percentage_1_std=len(list1_std)/len(m_final)*100
print("percentage is:",percentage_1_std)

for b in m_final :
   if b>two_std_start and b<two_std_end:
      list2_std.append(b)

percentage_2_std=len(list2_std)/len(m_final)*100
print("percentage is:",percentage_2_std)

for c in m_final :
    if c>third_std_start and c<third_std_end:
        list3_std.append(c)

percentage_3_std=len(list3_std)/len(m_final)*100
print("percentage is:",percentage_3_std)

#creating the displottt

fig=ff.create_distplot([m_final],["result"],show_hist=False)
fig.show()
