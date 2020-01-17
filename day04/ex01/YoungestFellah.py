import pandas as pd
from FileLoader import FileLoader

def youngestFellah(df, date):
    m_min = df.loc[(df['Year'] == date) & (df['Sex'] == 'M')].min()['Age']
    f_min = df.loc[(df['Year'] == date) & (df['Sex'] == 'F')].min()['Age']
    min_age = {'m' : m_min , 'f' : f_min}
    return (min_age)

f = FileLoader()
fl = f.load('../athlete_events.csv')
df = youngestFellah(fl, 2000)
print(df)
