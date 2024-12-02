weight=float(input("Enter weight in kg"))
height=float(input("Enter height in cm"))
height_meters=height/100 
BMI=weight/(height_meters**2)
print("Your BMI is:",BMI)
if BMI < 20.5:
    print("You're underweight")
elif 20.5<=BMI < 28:
    print("You're normalweight")
else:
    print("You're overweight")