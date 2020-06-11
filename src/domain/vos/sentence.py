import re

from src.domain.vos.abstractions.standard_value_object import StandardValueObject


class Sentence(StandardValueObject):
    """
    Sentences can contain:
    - alphanumeric symbols
    - spaces
    - hyphens
    - apostrophes
    """
    valid_pattern = re.compile(r'^[\w\' -]+$')

    def _validate_value(self, value: str):
        self._validate_type(obj=value, cls=str)
        value = value.strip()
        if not self.valid_pattern.match(value):
            raise self.InvalidSentence()

    class InvalidSentence(Exception):
        pass
