from datetime import datetime, timedelta

today = datetime.now()
number1 = 0
number2 = 0

def numbers():
  global number1
  global number2
  number1 = input("Please input a number:  ")
  number2 = input("Please input another number:  ")

def adding():
  numbers()
  result = float(number1)+ float(number2)
  print(number1, "+", number2, "=", result)

def subtracting():
  numbers()
  result = float(number1)- float(number2)
  print(number1, "-", number2, "=", result)

def multiplication():
  numbers()
  result = float(number1)* float(number2)
  print(number1,"X", number2, "=", result)

def division():
  numbers()
  result = float(number1)/ float(number2)
  print(number1, "divided by", number2, "=", result)

def age():
  year = input("Please enter your birthday in this format (YYYY-MM-DD):  ")
  try:
    birthday = datetime.strptime(birthday, "%Y-%m-%d")
    difference = today - birthday
    years = difference.days // 365
    print(f"You are {years} years old")
  except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD")


print("-----Welcome to the calculator-----\n")
option = input("Please choose an option from the menu below\n1.Adding\n 2.Subtracting\n 3.Multiplication\n 4.Division\n 5.Age calculator\n\n")
if option == "1":
  adding()
elif option == "2":
  subtracting()
elif option == "3":
  multiplication()
elif option == "4":
  division()
elif option == "5":
  age()
else:
  print("I dont recongise this function")

