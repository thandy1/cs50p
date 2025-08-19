def main():
    user_input = convert(input("What time is it? "))
    if 18 <= user_input <= 19:
        print("dinner time")
    elif 12 <= user_input <= 13:
        print("lunch time")
    elif 7 <= user_input <= 8:
        print("breakfast time")
    else:
        print("Invalid Input")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes/60
    
if __name__ == "__main__":
    main()
