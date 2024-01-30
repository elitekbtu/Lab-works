movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


def score(movies):
    name = input("Enter the name of the movie: ")
    for movie in movies:
        if movie["name"]==name:
            if movie["imdb"]>5.5:
                print("True")
            else:
                print("False")

score(movies)

def sublist(movies):
    result = []
    for movie in movies:
        if movie["imdb"]>5.5:
            result.append(movie["name"])
    print(result)
sublist(movies)

def categories(movies):
    film_category = input("Enter the category of the movie: ")
    result = []
    for movie in movies:
        if movie["category"]==film_category:
            result.append(movie["name"])
    print(result)

categories(movies)

def avrg(array, movies):
    result_name = []
    result_imdb = []
    for movie in movies:
        result_name.append(movie["name"])
        result_imdb.append(movie["imdb"])
    sum=0
    length = 0
    for cinema in array:
        if cinema in result_name:
            length+=1
            sum+=result_imdb[result_name.index(cinema)]

    print("Average of IMDB: ",sum/length)

avrg(['Usual Suspects', 'Hitman', 'Dark Knight', 'The Help', 'The Choice', 'Colonia', 'Love'], movies)


def c_avrg(category, movies):
    result = []
    for movie in movies:
        if movie["category"]==category:
            result.append(movie["imdb"])
    print("Average of the category: ",sum(result)/len(result))

c_avrg("Romance", movies)
    

    

