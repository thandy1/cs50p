def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else: 
        print("Odd")

def is_even(n):
    return n % 2 == 0
    
main()   

answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()

match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")