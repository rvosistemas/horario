from .entity import Entity


class Alarm(Entity):
    def __init__(
            self, id, name, created_at, updated_at, alarmType,
            soundPath, imagePath):
        super(Alarm, self).__init__(id, name, created_at, updated_at)
        self.alarmType = alarmType
        self.soundPath = soundPath
        self.imagePath = imagePath
