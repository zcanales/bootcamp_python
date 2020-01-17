import pandas as pd
from FileLoader import FileLoader

def howManyMedals(df, name):
    dict_res = {}
    for y in df.loc[df.Name == name].Year.unique():
        gold = len(df.loc[(df.Name == name) & (df.Medal == 'Gold') & (df.Year == y)])
        silver = len(df.loc[(df.Name == name) & (df.Medal == 'Silver') & (df.Year == y)])
        bronze = len(df.loc[(df.Name == name) & (df.Medal == 'Bronze') & (df.Year == y)])
        dict_res[y] = {'G' : gold, 'S' : silver, 'B' : bronze}
    print(dict_res)

f = FileLoader()
fl = f.load('../athlete_events.csv')
d = howManyMedals(fl, 'Kjetil Andr Aamodt')
