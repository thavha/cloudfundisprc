# To run the program :

## It is best to run the programm in newly created virtual environment

* run the command `pip install -r requirements.txt` to install the required depandencies
* this programm assumes that the file imdb_top_1000.csv is in the working directory
* there are number of required arguents needed to run the program, for more in formation on this run python challange.py -h
* the required arguments are --database(str), -- table(str), --seed(bool) and --query(str)
* the query argument can only contains one of the following [top_10_movies, top_10_actors, year, longest_movie, gross_year, find_movie]
* to find top 10 movies run challange.py with all the required arguments and --query tag set to top_10_movies i.e. python challenge.py --database test --table movies --seed True --query top_10_movies
* to find top 10 actors run python challenge.py --database test --table movies --seed True --query top_10_actors
