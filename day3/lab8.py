#Given a n-digit number. Find the sum of its 
number = int(input("Enter a number"))
sumOfDigits = 0
for digit in str(number):
 sumOfDigits += int(digit)
print(sumOfDigits)
