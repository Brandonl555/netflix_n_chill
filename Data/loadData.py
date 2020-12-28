import pandas as pd
import numpy as np

class load_Data:

    def __init__(self):
        #init shit
        self.data = None
        self.titles = None

    ### loads movei data from path into pandas dataframe
    def load_into_pd_df(self, path):
        self.data = pd.read_csv(path)
        self.titles = self.data['Title']
        self.write_to_csv(self.titles, 'movieTitles.csv')
        self.write_to_csv(self.data, 'allMovieData.csv')
        return self.data, self.titles

    def write_to_csv(self, data, name):
        data.to_csv(name)


#testing
ld = load_Data()
df, titles = ld.load_into_pd_df("IMDB-Movie-Data.csv")
print(df, titles)
print('I love sophie')
