from db.db import get_database

db = get_database()


class Fighter(db.Model):
    __tablename__ = 'fighters'
    fighter_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), unique=False, nullable=False)
    division = db.Column(db.String(64), unique=False, nullable=True)
    ranking = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return '<Fighter %r>' % self.full_name