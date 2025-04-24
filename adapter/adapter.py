class Projector:
    def turn_on(self):
        pass


class SamsungProjector:
    def on(self):
        print("SAMSUNG projector on")


class LgProjector:
    def enable(self):
        print('LG projector on')


class SamsungAdapter(Projector):
    def __init__(self, s_p: SamsungProjector) -> None:
        super().__init__()
        self.s_p = s_p

    def turn_on(self):
        self.s_p.on()


class LgAdapter(Projector):
    def __init__(self, l_p: LgProjector) -> None:
        super().__init__()
        self.l_p = l_p

    def turn_on(self):
        self.l_p.enable()


if __name__ == "__main__":
    s_p = SamsungProjector()
    l_p = LgProjector()

    s_adapter = SamsungAdapter(s_p)
    l_adapter = LgAdapter(l_p)

    s_adapter.turn_on()
    l_adapter.turn_on()
