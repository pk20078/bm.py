#BMI calc
weight = 63
height = 1.75
bmi = weight / height **2

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <=24.9:
    print("Normal")
elif bmi <= 25 and bmi >= 29.9:
    print("Overweight")
elif bmi >=30.0 and bmi <= 34.9:
    print("Obese")
elif bmi >= 35.0 and bmi <= 39.9:
    print(" Severely Obese")
elif bmi >= 40.0:
    print("Morbidly Obese")