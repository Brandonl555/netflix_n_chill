import pandas as pd
import numpy as np
import sys
class randomizer:

    def __init__(self, path, genre = None):
        #hello
        self.movies = None
        self.data = None
        self.moviePath = path
        self.genreParam = genre

    def selectRandomMovie(self):
        #load in all movie data, used for filtering if params given
        self.data = pd.read_csv(self.moviePath)

        #print(self.data['Genre'])
        if self.genreParam in self.data['Genre']: #TODO -> not properly checking for the genre
            #mySubstring =
            self.data.filter(regex=self.genreParam, axis = 1)
            currSample = self.data.sample()
            print(currSample['Title'])
            print(currSample['Genre'])
            print("Filtered by: " + self.genreParam)
        else:
            #selects random title from movieTitles data
            print(self.data['Title'].sample())
            print('Non-filtered results.')

params = sys.argv
#sanity check
#print(len(sys.argv))
#print(sys.argv)
if len(sys.argv) > 1:
    rd = randomizer("C:/Users/jungl/Downloads/personal_software_projs/netflix_n_chill/Data/allMovieData.csv", params[1])
else:
    rd = randomizer("C:/Users/jungl/Downloads/personal_software_projs/netflix_n_chill/Data/allMovieData.csv")
print("I love sophie")
rd.selectRandomMovie()
