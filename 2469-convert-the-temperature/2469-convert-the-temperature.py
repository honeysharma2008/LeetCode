class Solution(object):
    def convertTemperature(self, celsius):
        fahrenheit = celsius * 1.80 + 32.00
        kelvin = celsius + 273.15
        return [kelvin, fahrenheit]