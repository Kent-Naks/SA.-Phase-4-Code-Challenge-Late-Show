from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{"id": ep.id, "date": ep.date, "number": ep.number} for ep in episodes])

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        appearances = [
            {
                "id": ap.id,
                "rating": ap.rating,
                "episode_id": ap.episode_id,
                "guest_id": ap.guest_id,
                "guest": {
                    "id": ap.guest.id,
                    "name": ap.guest.name,
                    "occupation": ap.guest.occupation
                }
            }
            for ap in episode.appearances
        ]
        return jsonify({
            "id": episode.id,
            "date": episode.date,
            "number": episode.number,
            "appearances": appearances
        })
    return jsonify({"error": "Episode not found"}), 404
