from flask import Flask, render_template, request
import requests
api_key = 'ecc029db2174a909454b9bacebb4e6f4'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/recommender', methods= ["GET", "POST"])
def recommend():
    if request.method == "POST":
        artist = request.form['band']
        url = f'http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist={artist}&api_key={api_key}&format=json'
        response = requests.get(url)
        data = response.json()
        similar_artists = []
        for artist in data['similarartists']['artist']:
            similar_artists.append(artist['name'])
  
       
        return render_template('result.html', artists = similar_artists)
    return render_template('recommend_form.html')

if __name__ == '__main__':
    app.run(debug = True)