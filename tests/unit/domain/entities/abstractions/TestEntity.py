from unittest import TestCase

from src.domain.entities.abstractions.entity import Entity


class TestEntity(TestCase):
    example_id = 'example id'
    second_example_id = 'second example id'

    def setUp(self):
        self.entity = self.ExampleEntity(self.example_id)

    def test_representation(self):
        self.assertEqual(self.entity.__repr__(),
                         'unit.domain.entities.abstractions.TestEntity.ExampleEntity(example id)')

    def test_equality(self):
        self.assertTrue(self.entity == self.ExampleEntity(self.example_id))
        self.assertFalse(self.entity == self.ExampleEntity(self.second_example_id))
        self.assertFalse(self.entity == 'something else')
        self.assertFalse(self.entity == self.AnotherExampleEntity(self.example_id))

    def test_hash(self):
        self.assertIsInstance(self.entity.__hash__(), int)

    class ExampleEntity(Entity):
        def __init__(self, id_):
            self.id_ = id_

    class AnotherExampleEntity(Entity):
        def __init__(self, id_):
            self.id_ = id_
