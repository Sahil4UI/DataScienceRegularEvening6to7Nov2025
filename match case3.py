a = input("Enter Character : ")
match a:
    case "a" | "e" | "i" | "o" | "u":
        print("Vowels Detected")
    case _:print("Consonant Detected...")