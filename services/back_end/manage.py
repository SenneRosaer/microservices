from flask.cli import FlaskGroup

from users import create_app
from database.models import User
from database.models import db

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def seed_db():
    db.session.add(User(username='ss',email='senne.rosaer@telenet.be',password='ss'))
    db.session.commit()

if __name__ == '__main__':
    cli()