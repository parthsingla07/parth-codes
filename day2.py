marks = 55

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade F")
 
marks = int(input("Tumhare marks kitne hain? "))
if marks >= 90:
    print("Grade A - Excellent!")
elif marks >= 75:
    print("Grade B - Good!")
elif marks >= 60:
    print("Grade C - Average")
else:
    print("Grade F - Study harder!")

naam = input("Tumhara naam kya hai?")
age = int(input("Tumhari age kitni hai? "))
if age <18:
    print(naam + ", tum minor ho!")
elif age >= 18 and age <= 25:
    print(naam + ", tum young adult ho!" )
else:
    print(naam + ", tum adult ho!! ")

number = int(input("tumhara number kya hai? "))
if number > 0:       # sirf positive (0 nahi)
    print("Positive number hai!")
elif number < 0:     # sirf negative
    print("Negative number hai!")
else:                 # sirf 0 bachega
    print("Zero hai!")


firstnumber = int(input("tumhare pehla number kya hai? "))
secondnumber = int(input("tumhara dusra number kya hai? "))
operation = (input("btao kya operation karna hai?"))
if operation == "+":
    print(firstnumber + secondnumber)
elif operation == "-":
    print(firstnumber-secondnumber)
elif operation == "*":
    print(firstnumber*secondnumber)
elif operation == "/":
    print(firstnumber/secondnumber)
else:
    print("invalid operation")












