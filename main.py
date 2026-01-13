def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def main():
    print("Hello, Team!")
    result = divide(10, 2)
    print(f"Division result: {result}")

if __name__ == "__main__":
    main()