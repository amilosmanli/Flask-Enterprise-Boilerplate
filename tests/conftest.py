import pytest

from core.factories import create_app


@pytest.fixture
def app():
    print('Loading application')
    return create_app(__name__, 'testing')
