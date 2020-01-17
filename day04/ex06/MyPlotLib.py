import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy
import seaborn
from FileLoader import FileLoader
from HowManyMedalsByCountry import howManyMedalsByCountry

class MyPlotLib():
    def histogram(self, df, features):
        df.hist(features)
        plt.show()

    def density(self, df, features):
        df[features].plot.kde()
        plt.show()

    def pair_plot(self, data, features):
        seaborn.pairplot(data[features])
        plt.show()

        

    def box_plot(self, data, features):
        df.boxplot(features)
        plt.show()

f = FileLoader()
df = f.load('../athlete_events.csv')

mpl = MyPlotLib()
#h = mpl.histogram(df, ['Year', 'ID','Height'])
#i = mpl.density(df, ['Weight','Height'])
#j = mpl.pair_plot(df, ['Weight', 'Height'])
#k = mpl.box_plot(df, ['Weight','Height'])
