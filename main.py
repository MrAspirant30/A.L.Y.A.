from modules import bmi
from modules import calculator
from modules import command_center
from modules import length_converter

def show_banner():
 print("="*50)
 print("A.L.Y.A.".center(50))
 print("="*50)

def show_menu():
 print("1. BMI\n2. CALCULATOR\n3. COMMAND CENTER\n4. LENGTH CONVERTER(feet ---> cm)\n0. Exit\n")
def get_choice():
 return int(input())
def handle_choice(user_choice):
 match user_choice:
  case 1:
   bmi.run()
  case 2:
   calculator.run()
  case 3:
   command_center.run()
  case 4:
   length_converter.run()
  case 0:
   return False
  case _:
    print("Invalid Choice!")
 return True

while True:
 show_banner()
 show_menu()
 choice = get_choice()
 handle_choice(choice)
 if not handle_choice(choice):
    print("\nThank you for using A.L.Y.A. 👋")
    break
 