from flask import current_app

from app.data.models import User
from app.data.marshallers import UserSchema

logger = current_app.logger


class UserController:
    @classmethod
    def get(cls):
        return

    @classmethod
    def list(cls):
        users = User.query.all()
        current_app.logger.info("Users handler")
        schema = UserSchema()
        for user in users:
            print(user)
        return schema.dump(users, many=True).data
