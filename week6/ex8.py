text = input("Enter a text: ")
Letter =0
Digit =0
for i in text:
    if i.isdigit():
        Digit+=1
    elif i.isalpha():
        Letter+=1
print(f"The text is {text}")
print(f"Letter {Letter}")
print(f"Digit {Digit}")