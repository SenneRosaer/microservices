from flask.cli import FlaskGroup

from rating import create_rating_app
from database.models import User
from database.models import db

app = create_rating_app()
cli = FlaskGroup(create_app=create_rating_app)

@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def seed_db():
    #TODO aanpassen
    db.session.add(User(username='Senne',email='senne.rosaer@telenet.be',password='pwd'))
    db.session.commit()


if __name__ == '__main__':
    cli()