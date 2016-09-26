from flask import Flask, render_template

app = Flask(__name__)

# Create Movies along with show timings and showing for number of days
movie_list= {"Raaz": {"Morning": "10:00 AM", "Noon": "1:00 PM", "Evening": "4:30 PM"},
             "Baby": {"Morning": "11:00 AM", "Noon": "1:30 PM", "Evening": "5:30 PM"},
             "OMG": {"Morning": "10:15 AM", "Noon": "2:00 PM", "Evening": "6:45 PM", "Night": "9:45 PM"},
             'Guru': {'Morning': '11:10 AM', 'Noon': '2:00 PM', 'Evening': '5:15 PM', 'Night': '10:00 PM'}}

number_days_showing= {"Raaz": "10", "Baby": "20", "OMG": "30", "Guru": "18"}


# Display All available movies with details
@app.route('/', methods=['GET'])
def list_movies():
    return render_template("list_movies.html", movies= movie_list, days_showing=number_days_showing)


# Search func returns movie names showing greater than number of search days
@app.route('/search/<days>', methods=['GET'])
def show_days(days):
    available_movies = {}
    try:
        for movie_name, days_count in number_days_showing.items():
            if days_count >= days :
                available_movies[movie_name] = days_count
        return render_template("movie_availability.html", movie_avail= available_movies )
    except Exception:
        return "No search criteria exists for given days {}" .format(days)


# Search func returns show timing based on movie and show specified
@app.route('/search/<movie_name>/<show>', methods=['GET'])
def get_info(movie_name,show):
    try:
        movies = movie_list
        return render_template("show_time.html", movie_name=movie_name, show=show, show_time=movies[movie_name][show])
    except Exception:
        return "Invalid search criteria {} and/or show time {}".format(movie_name,show)


# Inserts Movie along with show time and Number of days movie available
@app.route('/addMovie')
def add_movie():
    add_movie1 = {'Go': {'Morning': '11:10 AM', 'Noon': '2:00 PM', 'Evening': '5:15 PM', 'Night': '10:00 PM'}}
    add_days = {"Go": "25"}
    try:
        movie_list.update(add_movie1)
        number_days_showing.update(add_days)
    except Exception:
        return "Unable to Update/Add Movie"
    return render_template("list_movies.html", movies=movie_list, days_showing=number_days_showing)


# Deletes Movie details along with show time and Number of days movie available
@app.route('/deleteMovie/<movie_name>')
def del_movie(movie_name):
    if movie_name in movie_list:
        del movie_list[movie_name]
    if movie_name in number_days_showing:
        del number_days_showing[movie_name]
    return render_template("list_movies.html", movies=movie_list, days_showing=number_days_showing)


if __name__ == '__main__':
    app.run(debug=True) # Debug mode