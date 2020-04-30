from src.domain.vos.abstractions.value_object import ValueObject


class Days(ValueObject):
    def _validate_value(self, value):
        """pass"""