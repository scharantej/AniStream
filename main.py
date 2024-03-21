
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.anime

@app.route('/')
def home():
    animes = db.animes.find()
    return render_template('index.html', animes=animes)

@app.route('/anime/<anime_id>')
def anime(anime_id):
    anime = db.animes.find_one({'_id': ObjectId(anime_id)})
    episodes = db.episodes.find({'anime_id': ObjectId(anime_id)})
    return render_template('anime.html', anime=anime, episodes=episodes)

@app.route('/anime/<anime_id>/episode/<episode_id>')
def episode(anime_id, episode_id):
    episode = db.episodes.find_one({'_id': ObjectId(episode_id)})
    return render_template('episode.html', episode=episode)

@app.route('/search', methods=['POST'])
def search():
    title = request.form['title']
    genre = request.form['genre']
    if title:
        animes = db.animes.find({'title': {'$regex': title, '$options': 'i'}})
    elif genre:
        animes = db.animes.find({'genre': genre})
    else:
        animes = db.animes.find()
    return render_template('index.html', animes=animes)

if __name__ == '__main__':
    app.run(debug=True)
