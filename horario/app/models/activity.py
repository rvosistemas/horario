from .entity import Entity


class Activity(Entity):
    def __init__(
            self, id, name, create_at, update_at, description, duration, hour,
            date, user_id, alarm_id, tag_id):
        super(Activity, self).__init__(id, name, create_at, update_at)
        self.description = description
        self.duration = duration
        self.hour = hour
        self.date = date
        self.user_id = user_id
        self.alarm_id = alarm_id
        self.tag_id = tag_id
