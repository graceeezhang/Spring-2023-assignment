from flask import Flask, render_template, request
import requests
api_key = '0f0f87f51dbba10af0d7a68a80b9404d'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/movie', methods= ["GET", "POST"])
def movie():
    if request.method == "POST":
        movie = request.form['band']
        url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie}'
        response = requests.get(url)
        data = response.json()
        movie_overview = []
        for movie in data['results']:
            movie_overview.append(movie['overview'])
  
       
        return render_template('result.html', movies = movie_overview)
    return render_template('movie.html')

if __name__ == '__main__':
    app.run(debug = True)