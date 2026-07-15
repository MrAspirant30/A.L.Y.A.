from modules import bmi
from modules import calculator
from modules import command_center
from modules import length_converter

def banner():
 print("="*50)
 print("A.L.Y.A.".center(50))
 print("="*50)
banner()

while True:
 choice = int(input("1. BMI\n2. CALCULATOR\n3. COMMAND CENTER\n4. LENGTH CONVERTER(feet ---> cm)\n0. Exit\n"))
 match choice:
  case 1:
   bmi.run()
  case 2:
   calculator.run()
  case 3:
   command_center.run()
  case 4:
   length_converter.run()
  case 0:
   break