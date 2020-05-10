from src.domain.vos.abstractions.flip_cards_sides_set import FlipCardSidesSet


class SecondarySet(FlipCardSidesSet):
    def _raise_exception(self):
        raise self.InvalidSecondaryBufferValueType()

    class InvalidSecondaryBufferValueType(FlipCardSidesSet.InvalidFlipCardSidesValueType):
        """pass"""