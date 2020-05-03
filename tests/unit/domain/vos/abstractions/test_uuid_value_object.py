from unittest import TestCase
from uuid import uuid4

from src.domain.vos.abstractions.uuid_value_object import UuidValueObject


class TestUuidValueObject(TestCase):
    invalid_id = 'invalid id'
    valid_id = uuid4()

    def test_invalid_day_plan_id__raise_exception(self):
        self.assertRaises(self.UuidVoImpl.InvalidUuid, self.UuidVoImpl, self.invalid_id)

    def test_valid_day_plan_id__return_exception(self):
        day_plan_id = self.UuidVoImpl(self.valid_id)

        self.assertEqual(day_plan_id.value, self.valid_id)

    class UuidVoImpl(UuidValueObject):
        def _raise_exception(self):
            raise self.InvalidUuid()

