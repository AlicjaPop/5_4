import random

class MoviesLibrary:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

        self._played_number=0

    def __str__(self):
        return f"{self.title} ({self.year})"
    
    @property
    def play(self):
        return self._played_number+1
    
class SeriesLibrary(MoviesLibrary):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f"{self.title} S{self.season_number:02d}E{self.episode_number:02d}"
    
    @property
    def play(self):
        return self._played_number+1
    
movies_and_series_list=[]

#Fakes
from faker import Faker
fake=Faker()

for i in range (100):
    title = fake.name()
    year = fake.year()
    genre = fake.company()
    Movie=MoviesLibrary(title, year, genre)
    movies_and_series_list.append(Movie)

for i in range (50):
    episode_number = i
    season_number = i + 1
    title = fake.name()
    year = fake.year()
    genre = fake.company()
    Series_episode=SeriesLibrary(episode_number,season_number,title,year,genre)
    movies_and_series_list.append(Series_episode)

#Filters
def get_movies(list):
    Movies_list=[]
    for i in list:
        if isinstance(i,MoviesLibrary)==True:
            Movies_list.append(i)
    return sorted(Movies_list, key=lambda i: i.title)
    
def get_series(list):
    Series_list=[]
    for i in list:
        if isinstance(i,SeriesLibrary)==True:
            Series_list.append(i)
    return sorted(Series_list, key=lambda i: i.title)

#Search
def search(title):
    search_list=[]
    for i in movies_and_series_list:
        if i.title == title:
            search_list.append(i)
    return search_list

#generate views
def generate_views():
    i=random.choice(movies_and_series_list)
    i._played_number=i._played_number+random.randint(1,100)
    return (i.title, i._played_number) #zastanowić się czy tak zostawić

#generate views x 10
def generate_views_10():
    for n in range (10):
        generate_views()

#top titles
def top_titles(content_type):
    sorted_by_views=sorted(movies_and_series_list, key=lambda i: i._played_number, reverse=True)
    Movies=[]
    Series=[]
    if content_type=="Movie":
        for i in sorted_by_views:
            if isinstance(i, MoviesLibrary):
                 Movies.append(i)
        return Movies[0:9]
    elif content_type=="Series":
        for i in sorted_by_views:
            if isinstance(i, SeriesLibrary):
                 Series.append(i)
        return Series[0:9]
    