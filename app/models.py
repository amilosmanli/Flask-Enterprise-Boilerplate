from core.extensions import db, ma


class User(db.Model):
    __table__ = db.Table('users', db.metadata,
                         autoload=True, autoload_with=db.engine)

    def __repr__(self):
        return '<User: %s>' % self.id


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
