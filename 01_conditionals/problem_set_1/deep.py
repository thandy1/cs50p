answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")


# Solution 2
"""
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()

match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
"""