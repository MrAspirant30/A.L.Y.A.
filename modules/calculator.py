# Basic calculator module
print("=" * 50)
print("Calculator Mode".center(50))
print("=" * 50)

# Calculator menu
while True :
 print("[A] Addition\n[B] Substraction\n[C] Multiplication\n[D] Division\n")
 choice = input("choice: ")
 match choice :
  case "A":
   a = float(input("\nEnter 1st number: "))
   b = float(input("\nEnter 2nd number: "))
   print(f"\n{a} + {b} = {a+b: .2f}")
  case "B":
   a = float(input("\nEnter 1st number: "))
   b = float(input("\nEnter 2nd number: "))
   print(f"\n{a} - {b} = {a-b: .2f}\n")
   print(f"{b} - {a} = {b-a: .2f}")
  case "C":
   a = float(input("\nEnter 1st number: "))
   b = float(input("\nEnter 2nd number: "))
   print(f"\n{a} x {b} = {a*b: .2f}\n")
  case "D":
   a = float(input("\nEnter 1st number: "))
   b = float(input("\nEnter 2nd number: "))
   print(f"\n{a} % {b} = {a/b: .2f}\n")
   print(f"{b} % {a} = {b/a: .2f}")
  case _:
   print("\nIncorrect choice!")
   


   