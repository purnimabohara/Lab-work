#Ask user to enter age,gender(M or F) and then using following rules print the place of their service
#if employee is female , then she will work only in urban areas
#if employee is male and age is between 20 to 40, then he will work anywhere.
#if employee is male and age ids between 40 to 60,then he will work in urban areas.
#And any other input of age will print "Error"
age = int(input("Enter the age"))
gender = int(input("Enter the gender : M or F"))
gender = gender.upper ()
if age >20 or age<60:
    print("ERROR")
elif gender== "F":
    result = "She will work in urban areas only"
elif age <40 and age >20:
    result= "He will work anywhere"
elif age <60 and age >40:
    result ="He will work in urban areas only"

