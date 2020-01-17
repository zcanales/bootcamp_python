import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy
import seaborn
from FileLoader import FileLoade

class Komparator():
    def __init__(self, df):
        self.df = df

    def compare_box_plts(self, cat_var, num_var):






f = FileLoader()
df = f.load('../athlete_events.csv')r
