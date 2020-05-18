from pytest import fixture
from horario.app.models import User


@fixture
def user():
    return User(
        id=1,
        name='richard',
        create_at='2013-01-15 10: 00',
        update_at='2013-01-15 10: 00',
        password='1198',
    )


def test_user_instantiation(user):
    assert user is not None


def test_user_attributes(user):
    assert user.id == 1
    assert user.name == 'richard'
    assert user.create_at == '2013-01-15 10: 00'
    assert user.update_at == '2013-01-15 10: 00'
    assert user.password == '1198'
