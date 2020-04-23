import re

from src.domain.vos.abstractions.value_object import ValueObject


class Sentence(ValueObject):
    """
    Sentences can contain:
    - alphanumeric symbols
    - spaces
    - hyphens
    - apostrophes
    """
    valid_pattern = re.compile(r'^[\w\' -]+$')

    def _validate_value(self, value: str):
        if not value:
            raise self.InvalidSentence()
        value = value.strip()
        if not self.valid_pattern.match(value):
            raise self.InvalidSentence()

    class InvalidSentence(Exception):
        pass
