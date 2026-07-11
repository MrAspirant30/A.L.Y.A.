#feet to cm
def banner():
 print("=" * 50)
 print("VERSION - 0.1".center(50))
 print("=" * 50)

banner()

feet = float(input("Enter length in feet: "))

cm = feet*30.48

print(f"{feet} in cm = {cm} cm")