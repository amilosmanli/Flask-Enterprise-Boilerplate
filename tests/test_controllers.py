from uuid import uuid4

from tests.factories import UserFactory
from database.models import UserSchema


class TestHealthController:
    def test__get_health(self, client, session):
        res = client.get('/api/health')
        assert res.status_code == 200
        assert res.json == {'status': 'OK'}


class TestUserController:
    def test__get_users(self, client, session):
        user = UserFactory.create(id=str(uuid4()), name='John')
        schema = UserSchema()
        res = client.get('/api/users')
        assert res.status_code == 200
        assert res.json == [schema.dump(user).data]