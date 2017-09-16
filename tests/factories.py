import factory
from faker import Factory as FakerFactory

from core.extensions import db
from database.models import User

faker = FakerFactory.create()


class SQLAlchemyModelFactory(factory.Factory):

    class Meta:
        abstract = True

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        session = db.session
        session.begin(nested=True)
        obj = model_class(*args, **kwargs)
        session.add(obj)
        session.commit()
        return obj


class UserFactory(SQLAlchemyModelFactory):

    class Meta:
        model = User

    id = factory.LazyAttribute(lambda x: faker.uuid4())
    name = factory.LazyAttribute(lambda x: faker.name())

