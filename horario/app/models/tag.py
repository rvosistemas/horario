from .entity import Entity


class Tag(Entity):
    def __init__(self, id, name, created_at, updated_at):
        super(Tag, self).__init__(id, name, created_at, updated_at)
