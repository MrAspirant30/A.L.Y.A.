while 1:
     print("=" * 50)
     print("A.L.Y.A. Command Centre".center(50))
     print("=" * 50)
     choice = input("\nA. Research on any topic\nB. Simulation of any hypothetical situation\nC. Discussion of any topic\n\nChoic: ")
     match choice:
        case "A" | "a":
            print("Let's research on the topic\n")
            print("Research.......")
        case "B" | "b":
            print("Tell me about the situation to be simulated\n")
            print("Simulating.......")
        case "C" | "c":
            print("Let's discuss on the topic\n") 
            print("Discussion.......")
        case "I'm done":
             print("Let's meet soon!")
             break
        case _:
         print("Tell me what you wanna do today or should I suggest something?")
