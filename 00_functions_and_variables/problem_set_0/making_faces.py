def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")

def main():
    message = input()
    result = convert(message)
    print(result)
    
main()