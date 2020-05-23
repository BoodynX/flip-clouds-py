from src.domain.vos.unique_flip_card_sides_container import UniqueFlipCardSidesContainer


class SecondarySet(UniqueFlipCardSidesContainer):
    def _raise_exception(self):
        raise self.InvalidSecondaryBoxValueType()

    class InvalidSecondaryBoxValueType(UniqueFlipCardSidesContainer.InvalidUniqueFlipCardSidesContainerValueType):
        """pass"""