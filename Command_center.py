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
    else:
        print("Tell me what you wanna do today or should I suggest something?")
