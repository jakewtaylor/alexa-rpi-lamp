from fauxmo.plugins import FauxmoPlugin
import RPi.GPIO as gpio

class RelayPlugin(FauxmoPlugin):
    """
    Initiates the plugin.
    """
    def __init__(self, name: str, port: int, channel: int) -> None:
        # set default state
        self.state = 'off'

        # get the channel pin map
        channelPinMap = self.get_channel_pin_dict()

        # store the channel and pin
        self.channel = channel
        self.pin = channelPinMap[channel]

        # initiate the GPIO pins
        gpio.setmode(gpio.BCM)
        gpio.setup(self.pin, gpio.OUT)

        # initiate parent class
        super().__init__(name=name, port=port)

    """
    Turns on the relay channel.
    """
    def on(self) -> bool:
        print('turning on')
        # adjust state
        self.state = 'on'

        try:
            # turn on the channel
            gpio.output(self.pin, gpio.LOW)

            return True
        except:
            self.state = 'unknown'
            return False

    """
    Turns off the relay channel.
    """
    def off(self) -> bool:
        print('turning off')
        # adjust state
        self.state = 'off'

        try:
            # turn off the channel
            gpio.output(self.pin, gpio.HIGH)

            return True
        except:
            self.state = 'unknown'
            return False

    """
    Gets the current state.
    """
    def get_state(self) -> str:
        return self.state

    """
    Returns a dictionary like:
    relay_channel -> BCM Pin
    """
    def get_channel_pin_dict(self):
        return {
            8: 2
        }