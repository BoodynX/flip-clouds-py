from datetime import datetime

from src.domain.vos.day import Day


class Day_Stub(Day):
    value = datetime(2020, 1, 1)

    def __init__(self):
        """pass"""
