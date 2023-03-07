import random
from datetime import datetime
from faker import Faker
fake=Faker()

class AllLibrary:
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
    
class MoviesLibrary(AllLibrary):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.year})"
    
    @property
    def play(self):
        return self._played_number+1

class SeriesLibrary(AllLibrary):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f"{self.title} S{self.season_number:02d}E{self.episode_number:02d}"
    
    @property
    def play(self):
        return self._played_number+1

Library=[]
Series_list=[]
Movies_list=[]
genres = ["Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Thriller"]

#Random/fake library content
for i in range (100):
    title = fake.unique.sentence(nb_words=3, variable_nb_words=True, ext_word_list=None)
    year = fake.year()
    genre = random.choice(genres)
    Movie=MoviesLibrary(title, year, genre)
    Library.append(Movie)

for i in range (100):
    episode_number = random.randint(1,20)
    season_number = random.randint(1,20)
    title = fake.unique.sentence(nb_words=3, variable_nb_words=True, ext_word_list=None)
    year = fake.year()
    genre = random.choice(genres)
    Series_episode=SeriesLibrary(episode_number,season_number,title,year,genre)
    Library.append(Series_episode)

# Filters
def get_movies(list):
    for i in list:
        if isinstance(i,MoviesLibrary)==True:
            Movies_list.append(str(i))
    result=sorted(Movies_list)
    return result
    
def get_series(list):
    for i in list:
        if isinstance(i,SeriesLibrary)==True:
            Series_list.append(str(i))
    result=sorted(Series_list)
    return result

# Search
def search(title):
    search_list=[]
    for i in Library:
        if i.title == title:
            search_list.append(str(i))
    return search_list

# generate views
def generate_views():
    i=random.choice(Library)
    i._played_number=i._played_number+random.randint(1,100)
    return ((i.title, i._played_number))

# generate views x 10
def generate_views_10():
    for n in range (10):
        generate_views()

# top titles
def top_titles(content_type,n):
    sorted_by_views=sorted(Library, key=lambda i: i._played_number, reverse=True)
    Movies=[]
    Series=[]
    if content_type=="Series":
        for i in sorted_by_views:
            if isinstance(i, SeriesLibrary)==True:
                 Series.append((str(i), i._played_number))
        return Series[0:n]
    elif content_type=="Movies":
        for i in sorted_by_views:
            if isinstance(i, MoviesLibrary)==True:
                 Movies.append((str(i), i._played_number))
        return Movies[0:n]
    
# Add Season
def add_season():
    title=input("Podaj tytuł serialu:")
    year=input("Podaj rok produkcji:")
    genre=input("Podaj gatunek:")
    season_number=input("Podaj numer sezonu:")
    number_of_episodes=int(input("Podaj liczbę odcinków:"))
    for i in range(number_of_episodes):
        Library.append(SeriesLibrary(title, year, genre, i+1, season_number,))
    print(f"Dodano sezon {season_number} (liczba odcinków:", number_of_episodes, f") serialu {title} do biblioteki")

# How many episodes
def series_no_episodes(title):
    x=[]
    for i in Library:
        if isinstance(i,SeriesLibrary)==True:
            if i.title==title:
                x.append(str(i))
    return print(f"Liczba odcinków serialu {title} w bibliotece:", len(x))
    
print("Biblioteka filmów")

generate_views_10()

today=datetime.today()
formatted_today=today.strftime("%d.%m.%Y")

print(f"Najpopolularniejsze filmy i seriale dnia {formatted_today}:")

print("Filmy:")
print(top_titles("Movies", 3))

print("Seriale:")
print(top_titles("Series", 3))