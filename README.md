# To run the program :

## It is best to run the programm in newly created virtual environment
### Anaconda python : conda create --name myenv
###                 : source activate myenv

### Python run : python3 -m venv myenv
###            : source myenv/bin/activate 

* run the command `pip install -r requirements.txt` to install the required depandencies
* this programm assumes that the file imdb_top_1000.csv is in the working directory
* there are number of required arguents needed to run the program, for more in formation on this run python challange.py -h
* the required arguments are --database(str), -- table(str), --seed(bool) and --query(str)

## Functionality
* 1. To see Top 10 movies based on IMDB rating run
`python challenge.py --database test --table movies --seed True --query top_10_movies`
* 2. To see Top 10 lead actors (Star1 field) based on their movies average IMDB rating run
`python challenge.py --database test --table movies --seed True --query top_10_actors`
* 3. To see all the movies from that year, sorted by IMDB rating run , year can be any year
`python challenge.py --database test --table movies --seed True --year 1990 --query year`
* 4. To see the longest running movie of the year, along with its runtime in hours run, year can be any year
`python challenge.py --database test --table movies --seed True --year 2019 --query longest_movie`
* 5. To see the year that had the highest grossing movies along with the average gross of movies that year run
`python challenge.py --database test --table movies --seed True --query gross_year`
* 6. To see all matching movies  based on any input of part of a movie name (e.g. lord of the rings) run, movie can be any phrase that is part of the movie name
`python challenge.py --database test --table movies --seed True --query find_movie --movie 'lord of the rings'`