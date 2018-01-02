from core.extensions import ma

from app.data.models import User


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User