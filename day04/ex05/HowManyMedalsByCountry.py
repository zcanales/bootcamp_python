import pandas as pd
from FileLoader import FileLoader

def howManyMedalsByCountry(df, country):
    dict_res = {}
    for y in df.loc[df.Team == country].Year.unique():
        gold = df.loc[(df.Team == country) & (df.Medal == 'Gold') & (df.Year == y)].Event.nunique()
        silver = df.loc[(df.Team == country) & (df.Medal == 'Silver') & (df.Year == y)].Event.nunique()
        bronze = df.loc[(df.Team == country) & (df.Medal == 'Bronze') & (df.Year == y)].Event.nunique()
        dict_res[y] = {'G' : gold, 'S' : silver, 'B' : bronze}
    print(dict_res)
    return(dict_res)

f = FileLoader()
df = f.load('../athlete_events.csv')
d = howManyMedalsByCountry(df, 'France')

