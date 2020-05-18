from pytest import fixture
from horario.app.models import Tag


@fixture
def tag():
    return Tag(
        id=1,
        name='ejercicio',
        create_at='2013-01-15 10: 00',
        update_at='2013-01-15 10: 00',
    )


def test_tag_instantiation(tag):
    assert tag is not None


def test_tag_attributes(tag):
    assert tag.id == 1
    assert tag.name == 'ejercicio'
    assert tag.create_at == '2013-01-15 10: 00'
    assert tag.update_at == '2013-01-15 10: 00'
