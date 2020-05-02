from datetime import datetime

from src.domain.vos.day import Day


class DayStub(Day):
    value = datetime(2020, 1, 1)

    def __init__(self):
        """pass"""