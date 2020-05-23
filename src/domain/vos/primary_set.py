from src.domain.vos.unique_flip_card_sides_container import UniqueFlipCardSidesContainer


class PrimarySet(UniqueFlipCardSidesContainer):
    def _raise_exception(self):
        raise self.InvalidPrimaryBoxValueType()

    class InvalidPrimaryBoxValueType(UniqueFlipCardSidesContainer.InvalidUniqueFlipCardSidesContainerValueType):
        """pass"""
