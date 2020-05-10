from src.domain.vos.abstractions.flip_cards_sides_set import FlipCardSidesSet


class DayPlanSet(FlipCardSidesSet):
    def _raise_exception(self):
        raise self.InvalidDayPlanSetValueType()

    class InvalidDayPlanSetValueType(FlipCardSidesSet.InvalidFlipCardSidesValueType):
        """pass"""
