print("To exit type \"exit\" ")
choice = input("Enter your choice(A/B/C):\nA. Research on any topic\nB. Simulation of any hypothetical situation\nC. Discussion of any topic\n")

while 1:
    if choice == "A" or "a" or "B" or "C" or "c":
     match choice:
        case "A" | "a":
            print("Let's research on the topic\n")
            break
        case "B" | "b":
            print("Tell me about the situation to be simulated\n")
            break
        case "C" | "c":
            print("Let's discuss on the topic\n")
            break
    elif choice == "exit" or "Exit":
            print("Tell me what you wanna do today or should I suggest what can we do today?\n")    
    else:
        print("Tell me what you wanna do today or should I suggest something?")

print("You've exited!")