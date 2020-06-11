from src.domain.vos.side import Side


class Side_Stub_Front(Side):
    value = Side.Type.FRONT

    def __new__(cls, *args, **kwargs):
        return Side(cls.value)


class Side_Stub_Back(Side):
    value = Side.Type.BACK

    def __new__(cls, *args, **kwargs):
        return Side(cls.value)
