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


@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{"id": g.id, "name": g.name, "occupation": g.occupation} for g in guests])

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    episode_id = data.get('episode_id')
    guest_id = data.get('guest_id')

    if not (1 <= rating <= 5):
        return jsonify({"errors": ["validation errors"]}), 400

    appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
    db.session.add(appearance)
    db.session.commit()
    return jsonify({
        "id": appearance.id,
        "rating": appearance.rating,
        "episode_id": appearance.episode_id,
        "guest_id": appearance.guest_id,
        "episode": {
            "id": appearance.episode.id,
            "date": appearance.episode.date,
            "number": appearance.episode.number
        },
        "guest": {
            "id": appearance.guest.id,
            "name": appearance.guest.name,
            "occupation": appearance.guest.occupation
        }
    }), 201
