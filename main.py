# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round((weight)/(height*height))
sentence = ""
if (bmi < 18.5):
    sentence = "underweight"
elif (bmi < 25):
    sentence = "normal weight"
elif (bmi < 30):
    sentence = "slightly overweight"
elif (bmi < 35):
    sentence = "obese"
else:
    sentence = "clinically obese"

print(f"Your bmi is {bmi}, you are {sentence}.")