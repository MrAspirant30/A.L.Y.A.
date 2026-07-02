choice = input("Enter your choice(A/B/C):\nA. Research on any topic\nB. Simulation of any hypothetical situation\nC. Discussion of any topic\n")

match choice:
    case "A" | "a":
        print("Let's research on the topic\n")
    case "B" | "b":
        print("Tell me about the situation to be simulated\n")
    case "C" | "c":
        print("Let's discuss on the topic\n")
    case _:
        print("Tell me what you wanna do today\n")
