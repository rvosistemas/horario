from pytest import fixture
from horario.app.models import Entity


@fixture
def entity():
    return Entity(
        id=1,
        name='correr',
        create_at='2013-01-15 10: 00',
        update_at='2013-01-15 10: 00',
    )


def test_entity_creation(entity):
    assert isinstance(entity, Entity)


def test_entity_default_attributes(entity):
    assert entity.id == 0
    assert entity.name == ''
    assert entity.created_at == ''
    assert entity.updated_at == ''
