from core.extensions import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<User: %s>' % self.id

