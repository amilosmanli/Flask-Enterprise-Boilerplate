from app.models import User, UserSchema
from flask import current_app

logger = current_app.logger

def get_users():
    users = User.query.all()
    current_app.logger.info("Users handler")
    schema = UserSchema()
    for user in users:
        print(user)
    return schema.dump(users, many=True).data
