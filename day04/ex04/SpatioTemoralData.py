import pandas as pd
from FileLoader import FileLoader


class SpatioTemporalData():
    

    def __init__(self, df):
        self.df = df

    def when(self, location):
        time = list(self.df.loc[(self.df.City == location)].Year.unique())
        print(time)
        return(time)
    
    def where(self, date):
        place = list(self.df.loc[self.df.Year == date].City.unique())
        print(place)
        return(place)

f = FileLoader()
fl = f.load('../athlete_events.csv')
space = SpatioTemporalData(fl)
#time = space.when('Athina')
place = space.where(2016)
