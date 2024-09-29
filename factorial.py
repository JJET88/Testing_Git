num = int(input("Enter a number: "))
result =1
if num ==0 or num==1:
    result=1
else:
    for i in range(1,num+1):
        
        result *=i
print(f"The factorial of {num} is {result}")