from .entity import Entity


class Alarm(Entity):
    def __init__(
            self, id, name, create_at, update_at, alarmType,
            soundPath, imagePath):
        super(Alarm, self).__init__(id, name, create_at, update_at)
        self.alarmType = alarmType
        self.sound = soundPath
        self.image = imagePath
