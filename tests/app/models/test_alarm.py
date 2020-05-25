from pytest import fixture
from horario.app.models import Alarm


@fixture
def alarm():
    return Alarm(
        id=1,
        name='correr',
        created_at='2013-01-15 10: 00',
        updated_at='2013-01-15 10: 00',
        alarmType='recurrente',
        soundPath='./statics/sound/sonido.mp3',
        imagePath='./statics/img/foto.jpg',
    )


def test_alarm_instantiation(alarm):
    assert alarm is not None


def test_alarm_attributes(alarm):
    assert alarm.id == 1
    assert alarm.name == 'correr'
    assert alarm.created_at == '2013-01-15 10: 00'
    assert alarm.updated_at == '2013-01-15 10: 00'
    assert alarm.alarmType == 'recurrente'
    assert alarm.soundPath == './statics/sound/sonido.mp3'
    assert alarm.imagePath == './statics/img/foto.jpg'
