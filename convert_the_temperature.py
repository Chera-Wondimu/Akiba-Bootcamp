class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.8 + 32
        return [Kelvin, Fahrenheit]
celsius = float(input("Enter temperature in Celsius: "))
solution = Solution()
result = solution.convertTemperature(celsius)
print(result)