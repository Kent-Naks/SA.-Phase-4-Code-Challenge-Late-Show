import csv
from models import db, Episode, Guest, Appearance
from app import app

def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()

        with open('the_show.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                guest = Guest(name=row['Raw_Guest_List'], occupation=row['GoogleKnowlege_Occupation'])
                db.session.add(guest)
                db.session.commit()

                episode = Episode(date=row['YEAR'], number=row['Show'])
                db.session.add(episode)
                db.session.commit()

                appearance = Appearance(rating=5, episode_id=episode.id, guest_id=guest.id)
                db.session.add(appearance)

            db.session.commit()
