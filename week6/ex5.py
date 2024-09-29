number =[1,2,3,4,5,6,7,8,9]
even_num =0
odd_num=0

for i in number:
    if i%2==0:
        even_num+=1
    else:
        odd_num+=1

print(f"Number of even number {even_num}")
print(f"Number of odd number {odd_num}")