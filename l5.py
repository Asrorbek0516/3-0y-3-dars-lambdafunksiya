def celsius_to_fahrenheit(celsius):
    result = lambda c: (c * 9/5) + 32

    return result(celsius)


print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(25))
print(celsius_to_fahrenheit(100))
