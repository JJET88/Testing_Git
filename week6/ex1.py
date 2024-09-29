def TempConverter(Fahrenheit):
    result = round((5/9)*(Fahrenheit-32),1)
    print(f"The temperature is {result} degree Celsius")
    
Fahrenheit = float(input("Enter temperature in Farenheit: "))

TempConverter(Fahrenheit)