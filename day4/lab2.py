#Write a python program to sum three given integers.However if two or more value are equal sum will be
a= int(input("Enter the first number"))
b= int(input("Enter the second number"))
c= int(input("Enter the third number"))
if a==b or b==c or a==c:
    answer= 0
else:
    answer= a+b+c
    print(answer)