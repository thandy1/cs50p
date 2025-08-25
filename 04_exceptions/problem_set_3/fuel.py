def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            percentage = conversion(fraction)
            
        except (ValueError, ZeroDivisionError):
            continue

        else:
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break

def conversion(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError

    if x < 0 or x > y:
        raise ValueError

    return round(x/y * 100)

main()