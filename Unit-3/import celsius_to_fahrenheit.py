def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15


def main():
    print("Temperature Conversion Options:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")

    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C")

    elif choice == "3":
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius:.2f}°C is equal to {kelvin:.2f}K")

    else:
        print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()