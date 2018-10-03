from fauxmo.plugins import FauxmoPlugin

class TestPlugin(FauxmoPlugin):
    def __init__(self, name: str, port: int) -> None:
        self.state = 'off'

        super().__init__(name=name, port=port)

    def on(self) -> None:
        self.state = 'on'
        print('On!')

    def off(self) -> None:
        self.state = 'off'
        print('Off!')

    def get_state(self) -> str:
        return self.state