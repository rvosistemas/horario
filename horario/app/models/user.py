from .entity import Entity


class User(Entity):
    def __init__(self, id, name, created_at, updated_at, password):
        super(User, self).__init__(id, name, created_at, updated_at)
        self.password = password
