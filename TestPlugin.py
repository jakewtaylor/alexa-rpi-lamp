from fauxmo.plugins import FauxmoPlugin

class TestPlugin(FauxmoPlugin):
    def __init__(self, name: str, port: int) -> None:
        self.state = 'off'

        super().__init__(name=name, port=port)

    def on(self) -> bool:
        self.state = 'on'
        print('On!')
        return true

    def off(self) -> bool:
        self.state = 'off'
        print('Off!')
        return true

    def get_state(self) -> str:
        return self.state