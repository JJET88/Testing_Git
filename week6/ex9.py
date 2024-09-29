human_years = int(input("Enter a dog's age in human years: "))

if human_years <=2:
    dog_years = human_years *10.5
else:
    dog_years =(2* 10.5) + (human_years-2)*4

print(f"The dog's age in dog years is: {dog_years}")