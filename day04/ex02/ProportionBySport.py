import pandas as pd
from FileLoader import FileLoader

def proportionBySport(df, date, sport, sex):
   player_tot = len(df.loc[(df['Year'] == date) & (df['Sex'] == sex)].Name.unique())
   player_spe = len(df.loc[(df['Year'] == date) & (df['Sex'] == sex) & (df['Sport'] == sport)].Name.unique())
   print(player_spe / player_tot)

f = FileLoader()
fl = f.load('../athlete_events.csv')
df = proportionBySport(fl, 2004,'Tennis', 'F')
