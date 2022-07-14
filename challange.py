#!/usr/bin/python

import sqlite3, argparse
import pandas as pd


class TopMoviesAanalysis:
    def __init__(self, database, table, seed, query, year=0, movie=""):

        self.database = database
        self.table = table
        self.seed = seed
        self.year = year
        self.query = query
        self.movie = movie

    def setting_database(self):

        with sqlite3.connect(f"{self.database}.db") as db:
            db.commit()
        
   
    def loading_data(self):
        with sqlite3.connect(f"{self.database}.db") as db:
            c = db.cursor()
            c.execute(f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{self.table}'")
            
            if self.seed and c.fetchone()[0]==0:
                df = pd.read_csv("imdb_top_1000.csv")
                #remove row with no title
                df.drop(df[df.Series_Title == ""].index, inplace=True)
                #droping any duplicates
                df.drop_duplicates(keep=False, inplace=True)
                #removing min from runtime column
                df['Runtime'] = df['Runtime'].str.replace("min", "")
                df = df.astype({"Runtime":int})
                df.to_sql(name = self.table, con = db, if_exists= "replace")
                db.commit()
    def top_ten_movies_based_on_imdb_rating(self):

        with sqlite3.connect(f"{self.database}.db") as db:

            c = db.cursor()
            
            results = c.execute(f"SELECT Series_Title AS Movie_title, IMDB_Rating AS IMDB_rating FROM {self.table} ORDER BY 2 DESC LIMIT 10")
            return results.fetchall()

    def  top_ten_lead_actors_based_on_imdb_rating(self):
        with sqlite3.connect(f"{self.database}.db") as db:
            c = db.cursor()
            results = c.execute(f"SELECT Star1 AS Lead_actor, IMDB_Rating AS IMDB_rating FROM {self.table} ORDER BY 2 DESC LIMIT 10")
            return results.fetchall()

    def movies_of_the_year(self):
        with sqlite3.connect(f"{self.database}.db") as db:
            c = db.cursor()
            results = c.execute(f"SELECT Series_Title AS Movie_title, IMDB_Rating AS IMDB_rating FROM {self.table} WHERE Released_Year = {self.year} ORDER BY 2 DESC")
            return results.fetchall()

    def longest_running_movie(self):
        with sqlite3.connect(f"{self.database}.db") as db:
            c = db.cursor()
            results = c.execute(f"SELECT Series_Title AS Movie_title, Round(Max(Runtime)/60.00, 2) AS Runtime_hours FROM {self.table} WHERE Released_Year = {self.year}")
            return results.fetchall()

    def year_with_highest_gross(self):
        with sqlite3.connect(f"{self.database}.db") as db:
            c = db.cursor()
            results = c.execute(f"SELECT Released_Year AS year, AVG(Gross) AS Avarage_gross_in_dollars FROM {self.table} GROUP BY Released_Year ORDER BY Avarage_gross_in_dollars DESC LIMIT 1")
            return results.fetchall()

    def movies_like(self):
        with sqlite3.connect(f"{self.database}.db") as db:
            c = db.cursor()
            print(self.movie)
            results = c.execute(f"SELECT Series_Title AS Movie_title, IMDB_Rating AS IMDB_rating FROM {self.table} WHERE Movie_title LIKE '%{self.movie}%'")
            return results.fetchall()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='database properties and query properties')
    parser.add_argument("--database", type= str, metavar = "", required= True, help= "The name that will be used when creating the database")
    parser.add_argument("--table", type= str, metavar = "", required= True, help= "The name that will be used when creating the table on the database")
    parser.add_argument("--seed", type= bool, metavar = "", required= True, help= "set to True to load the data only obce")
    parser.add_argument("--query", type= str, metavar = "", required= True, help= "query description to be used")
    parser.add_argument("--year", type= int, metavar = "", required= False, help= "year to filter the query")
    parser.add_argument("--movie", type= str, metavar = "", required= False, help= "search for movies that contains the phrase")
    args = parser.parse_args()
    movies_instance = TopMoviesAanalysis(args.database, args.table, args.seed, args.query, args.year, args.movie)
    movies_instance.setting_database()
    movies_instance.loading_data()
    if args.query == "top_10_movies":
        print(movies_instance.top_ten_movies_based_on_imdb_rating())
    elif args.query == "top_10_actors":
        print(movies_instance.top_ten_lead_actors_based_on_imdb_rating())
    elif args.query == "year":
        print(movies_instance.movies_of_the_year())
    elif args.query == "longest_movie":
        print(movies_instance.longest_running_movie())
    elif args.query == "gross_year":
        print(movies_instance.year_with_highest_gross())
    elif args.query == "find_movie":
        print(movies_instance.movies_like())