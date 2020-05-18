from pytest import fixture
from horario.app.models.activity import Activity


@fixture
def activity():
    return Activity(
        id=1,
        name='correr',
        create_at='2013-01-15 10: 00',
        update_at='2013-01-15 10: 00',
        description='correr en 30 min',
        duration='00: 00: 00',
        hour='00: 00: 00',
        date='2013-01-15',
        user_id=1,
        alarm_id=1,
        tag_id=1,
    )


def test_activity_instantiation(activity):
    assert activity is not None


def test_activity_attributes(activity):
    assert activity.id == 1
    assert activity.name == 'correr'
    assert activity.create_at == '2013-01-15 10: 00'
    assert activity.update_at == '2013-01-15 10: 00'
    assert activity.description == 'correr en 30 min'
    assert activity.duration == '00: 00: 00'
    assert activity.hour == '00: 00: 00'
    assert activity.date == '2013-01-15'
    assert activity.user_id == 1
    assert activity.alarm_id == 1
    assert activity.tag_id == 1
