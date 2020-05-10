from src.domain.vos.abstractions.flip_cards_sides_set import FlipCardSidesSet


class PrimarySet(FlipCardSidesSet):
    def _raise_exception(self):
        raise self.InvalidPrimaryBufferValueType()

    class InvalidPrimaryBufferValueType(FlipCardSidesSet.InvalidNewFlipCardsBufferValueType):
        """pass"""