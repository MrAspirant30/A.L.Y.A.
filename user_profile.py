import random

def banner():
 print("=" * 50)
 print("VERSION - 0.1".center(50))
 print("=" * 50)

# Displays the A.L.Y.A. version banner
banner()

# Different greetings shown randomly at startup
greetings = [
    "Ready to assist you today.",
    "Let's get started.",
    "How can I help you today?",
    "Hope you're having a productive day.",
    "Awaiting your instructions.",
    "Ready when you are.",
    "Let's build something today.",
    "Everything is set. What's next?",
    "What would you like to work on today?",
    "I'm listening."
]

print("\nHello, I'm A.L.Y.A.\n")

# Display a random greeting each time A.L.Y.A. start
print(random.choice(greetings))

# Collect user information
name= input("\nWhat's your name?")
print(f"Welcome, {name}. It's nice to meet you!\n")

print("I'm gonna ask you some questions to build your profile in my database\n")

age= int(input("What is your age?\n"))
fav_prog_lang= str(input("What is your favourite programming language?\n"))
adress= str(input("How should I adress you?\n"))

print("Your profile dasboard:\n")
print(f"{adress},\nYou are {age} year old and your favourite programming language is {fav_prog_lang}\nCorrect me if I'm wrong!")