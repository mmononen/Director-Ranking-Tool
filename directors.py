# Director Ranking Tool
# by Mikko Mononen

# Analyzes ratings.csv exported from IMDb.com and prints out the list of user's favorite movie directors.

# Usage: python directors.py >output.csv
# Import output.csv in Excel or equivalent and sort by weighted rating

import csv

# opens a csv file and returns it as a list
def open_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return list(reader)

# populate and return a dict of directors with names and ratings
# output dict: director name : a list of ratings
def populate_directors_dict(movies, directors):
    for m in movies:
        if m[5] == 'movie':       
            dirs = m[12].split(", ")
            for d in dirs:
                if d in directors:
                    directors[d] += [int(m[1])]
                    directors[d].sort(reverse=True)
                else:
                    directors[d] = [int(m[1])]
    return directors

# returns the number of movies in a movie list
def num_of_movies(movies):
    i = 0
    for m in movies:
        if m[5] == 'movie':
            i += 1
    return i

# returns the sum of all movie ratings in a movie list
def sum_of_ratings(movies):
    i = 0
    for m in movies:
        if m[5] == 'movie':
            i += int(m[1])
    return i

# calculate a weighted average for directors dict
# input: directors (dict), required amount of movies (int)
def calculate_weighted_average(directors, req_movies):
    for xd in directors:
        if (len(directors[xd]) >= req_movies):
            tempsum = 0
            for t1 in directors[xd]:
                tempsum += int(t1)
            R =  tempsum / len(directors[xd]) # average rating for director's movies
            v = len(directors[xd]) # number of director's movies
            C = sum_of_ratings(movies) / num_of_movies(movies) # the average rating of every film
            m = req_movies # minimum of films required (default = 3)
            W = (R*v + C*m) / (v + m) # weighted average
            print(xd + ";" + str(W) + ";" + str(v) + ";" + str(directors[xd]))

directors = {}
movies = open_csv('ratings.csv')

populate_directors_dict(movies, directors)
calculate_weighted_average(directors, 3)