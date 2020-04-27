from src.domain.vos.abstractions.value_object import ValueObject


class CardSetCount(ValueObject):
    min_count = 5
    max_count = 50

    def _validate_value(self, value: int):
        if not self.min_count <= value <= self.max_count:
            raise self.InvalidCardSetCount

    class InvalidCardSetCount(Exception):
        pass