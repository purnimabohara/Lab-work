#find factorial of a number
num=int(input("Enter the number"))
result=1
i=1
while i<=num:
    result*=i
    i+=1
print(f"The factorial of {num} is {result}.")