from .entity import Entity


class Tag(Entity):
    def __init__(self, id, name, create_at, update_at):
        super(Tag, self).__init__(id, name, create_at, update_at)
