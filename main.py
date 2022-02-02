import plotly.figure_factory as ff 
import plotly.graph_objects as go
import statistics 
import pandas as pd
import csv
import random

file=pd.read_csv("data.csv")
data=file["reading_time"].tolist()
fig=ff.create_distplot([data],["Reading Time"],show_hist=False)
fig.show()

mean=statistics.mean(data)
std=statistics.stdev(data)
print(mean)
print(std)

def random_setofmean(counter):
    dataset=[]
    for i in range(0,counter):
        rindex=random.randint(0,len(data)-1)
        value=data[rindex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

meanlist=[]
for i in range(0,100):
    setofmean=random_setofmean(30)
    meanlist.append(setofmean)

meanofmeanlist=statistics.mean(meanlist)
stdofmeanlist=statistics.stdev(meanlist)
fstdstart,fstdend=mean-stdofmeanlist,mean+stdofmeanlist
sstdstart,sstdend=mean-(stdofmeanlist*2),mean+(stdofmeanlist*2)
tstdstart,tstdend=mean-(stdofmeanlist*3),mean+(stdofmeanlist*3)

fig=ff.create_distplot([meanlist],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[fstdend,fstdend],y=[0,0.17],mode="lines",name="FISRT STANDARD DEVIATION"))
fig.add_trace(go.Scatter(x=[sstdend,sstdend],y=[0,0.17],mode="lines",name="SECOND STANDARD DEVIATION"))
fig.add_trace(go.Scatter(x=[tstdend,tstdend],y=[0,0.17],mode="lines",name="THIRD STANDARD DEVIATION"))
fig.show()

z_score=(meanofmeanlist-mean)/std
print(z_score)