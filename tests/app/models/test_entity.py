from pytest import fixture
from horario.app.models import Entity


@fixture
def entity():
    return Entity(
        id=1,
        name='correr',
        created_at='2013-01-15 10: 00',
        updated_at='2013-01-15 10: 00',
    )


def test_entity_creation(entity):
    assert isinstance(entity, Entity)


def test_entity_default_attributes(entity):
    assert entity.id == 1
    assert entity.name == 'correr'
    assert entity.created_at == '2013-01-15 10: 00'
    assert entity.updated_at == '2013-01-15 10: 00'
