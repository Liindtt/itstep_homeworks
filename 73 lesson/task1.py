class CelsiusTemperatureSensor:
    def __init__(self):
        self._temperature = None

    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_temperature_celsius(self):
        return self._temperature


class FahrenheitTemperatureSensor:
    def __init__(self):
        self._temperature = 77

    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_temperature_fahrenheit(self):
        return self._temperature


class TemperatureSensorAdapter:
    def __init__(self, fahrenheit: FahrenheitTemperatureSensor):
        self._fahrenheit = fahrenheit

    def get_temperature_celsius(self):
        return (self._fahrenheit.get_temperature_fahrenheit() - 32) / 1.8


def display_temperature(sensor):
    print(f"Temperature: {sensor.get_temperature_celsius():.2f} °C")


fahrenheit = FahrenheitTemperatureSensor()
fahrenheit_adapter = TemperatureSensorAdapter(fahrenheit)
celsium = CelsiusTemperatureSensor()
celsium.set_temperature(28)

display_temperature(fahrenheit_adapter)
display_temperature(celsium)
