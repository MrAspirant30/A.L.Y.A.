print("=" * 50)
print("VERSION - 0.1".center(50))
print("=" * 50)
print("Hello, I'm A.L.Y.A.\n")

name= input("What's your name?\n")
print(f"Welcome, {name}. It's nice to meet you!\n")

print("I'm gonna ask you some questions to build your profile in my database\n")

age= int(input("What is your age?\n"))
fav_prog_lang= str(input("What is your favourite programming language?\n"))
adress= str(input("How should I adress you?\n"))

print("Your profile dasboard:\n")
print(f"{adress},\nYou are {age} year old and your favourite programming language is {fav_prog_lang}\nCorrect me if I'm wrong!")