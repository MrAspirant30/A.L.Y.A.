def run():
 print("="*50)
 print("BMI Mode".center(50))
 print("="*50)

 # Calculate Body Mass Index (BMI)
 height = float(input("Height(in cm):\n"))
 weight = float(input("Weight(in Kg):\n"))

 print(f"BMI = {weight*10000/(pow(height, 2)): .2f} Kg/m^2")