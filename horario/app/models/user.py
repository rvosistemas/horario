from .entity import Entity


class User(Entity):
    def __init__(self, id, name, create_at, update_at, password):
        super(User, self).__init__(id, name, create_at, update_at)
        self.password = password
