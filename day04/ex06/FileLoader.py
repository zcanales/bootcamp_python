import pandas as pd

class FileLoader():
    def load(self, path):
        df = pd.read_csv(path)
        print ("Size of file is %s." % str(df.shape))
        return(df)

    def display(self, df, n):
        if n > 0:
            print(df.head(n))
        else:
            print(df.tail(-n))
