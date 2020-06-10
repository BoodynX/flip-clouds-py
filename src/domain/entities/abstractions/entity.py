from abc import ABC


class Entity(ABC):
    # This is meant to be overshadowed in the __init__
    id_ = None

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id_})'

    def __eq__(self, other):
        if isinstance(other, Entity):
            return self.id_ == other.id_
        else:
            return False

    def __hash__(self):
        return hash(self.id_)
