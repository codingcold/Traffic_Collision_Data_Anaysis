import matplotlib.pyplot as plt
import pandas as pd
import plotly.offline as py
import seaborn as sns

py.init_notebook_mode(connected=True)

location = []
age = []
time = []
latitudes = []
longitudes = []
df = pd.read_csv("Traffic_Collision_Data_from_2010_to_Present.csv")
# plot victim age
plt.hist(df["Victim Age"],bins=10)
plt.title("age analysis")
plt.xlabel("age")
plt.ylabel("rate")
plt.show()
#plot collisions per year
plt.subplots(figsize = (20,5))
# We have skiped 2020 because it doesn't have the entire year's data.
df1 = df[(df['Date Occurred'].isin(['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']))]
sns.countplot(df['Date Occurred'])
plt.title('Collisions per year')
# sns.countplot(df['Date Occurred'])
plt.show()
# Location of collisions
df['Premise Description'].value_counts().head(10)
#Collisions by age group
plt.subplots(figsize = (15,7))
sns.countplot(df['Victim Age'].sort_values(ascending = False))
plt.title('Collisions by Victim Age')
plt.xticks(rotation = 90)
plt.show()
#Collisions by time of day
import datetime as dt
def convert(x):
  return dt.datetime.strptime(x, '%H:%M')

def getTime(t):
    t = str(t)
    if len(t)==1:
      return t[0]+':'+'00'
    if len(t)<4:
      return t[:1] + ':' + t[1:]
    else:
      return t[:2] + ':' + t[2:]
df['Time Occurred']= df['Time Occurred'].apply(getTime)
df['Time Occurred']=df['Time Occurred'].apply(convert)
hours = [t.hour for t in df['Time Occurred'] ]
numbers=[x for x in range(0,24)]
labels=map(lambda x: str(x), numbers)
plt.subplots(figsize = (15,6))
sns.countplot(hours)




