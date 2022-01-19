print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
  print("you can ride the rollercoaster")
  age = int(input("How old are you?"))
  if age < 12:
    bill = 5
  elif age < 18:
    bill = 7
  else:
    bill = 10
  photo = (input("do you want a picture of your ride? (Y for yes, false for No)"))
  if photo == "Y":
    bill += 3
  print (f"Your total bill is ${bill}")
  
else:
  print("Sorry, you have to grow taller to ride the rollercoaster")