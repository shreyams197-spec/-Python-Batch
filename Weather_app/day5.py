# weight=float(input("Enter weight in kg:"))
# height=float(input("Enter height in meters:" ))
# bmi=weight/(height**2)

# if bmi < 18.5:
#     category = "Underweight"
# elif bmi < 25:
#     category = "Normal"
# elif bmi < 30:
#     category = "Overweight"
# else: category = "Obese"
# print("BMI:",bmi)
# print("category:",category)    

# units = int(input("Enter number units used:"))

# if units <= 100:
#     bill = units*1
# elif units <= 200:
#     bill = 100*1+(units-100)*2
# else:
#     bill = 100*1+100*2+(units-200)*5
#     print("Electricity Bill:$",bill)


a = int(input("Enter first angle:"))
b = int(input("Enter second angle:"))
c = int(input("Enter third angle:"))

if a==b and b==c and c==a:
    print("Equiatera triangle")
elif a==b or b==c or a==c:
    print("Isosceles triangle")
else:
    print("scalene traiangle")
