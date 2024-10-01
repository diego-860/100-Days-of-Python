weight = input("What is your weight in kilograms?\n")
height = input("What is your height in centimeters?\n")
bmi = float(weight) / (float(height) ** int(2))
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
if bmi >= 18.5:
    if bmi < 25:
        print(f"Your BMI is {bmi}, you have a normal weight.")
if bmi >= 25:
    if bmi < 30:
        print(f"Your BMI is {bmi}, you are slightly overweight.")
if bmi >= 30:
    if bmi < 35:
        print(f"Your BMI is {bmi}, you are obese.")
if bmi >= 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")
