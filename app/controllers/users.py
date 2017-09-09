from app.models import User, UserSchema


def get_users():
    users = User.query.all()
    schema = UserSchema()
    for user in users:
        print(user)
    return schema.dump(users, many=True).data
