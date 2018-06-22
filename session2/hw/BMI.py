h_cm = float(input("height?(cm) "))
h = (h_cm) / 100
m = float(input("weight?(kg) "))
BMI = (m) / (h*h)
if BMI < 16:
    print("severely underweight")
elif 16 < BMI < 18.5:
    print("underweight")
elif 18.5 < BMI < 25:
    print("normal")
elif 25 < BMI < 30:
    print("overweight")
elif BMI > 30:
    print("obese")