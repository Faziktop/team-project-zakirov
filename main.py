def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def main():
    print("Hello, Team!")
    
    # Тестируем обе функции
    mul_result = multiply(5, 3)
    div_result = divide(10, 2)
    
    print(f"Multiplication: {mul_result}")
    print(f"Division: {div_result}")

if __name__ == "__main__":
    main()