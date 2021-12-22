#accepts a string and calculate the number of digits and letters
word = input("Enter the combination")
d=0
l=0
for i in word:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        l+=1
print(f"There are {d} digits and {l} letters in {word}")