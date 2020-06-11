from tests.unit.domain.exceptions import InvalidType


def tc(obj: object, cls: type):
    if not isinstance(obj, cls):
        raise InvalidType()
