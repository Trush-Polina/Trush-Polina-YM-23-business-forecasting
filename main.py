def calculator():
    print("Простий калькулятор")
    
    try:
        num1 = float(input("Введіть перше число: "))
        operation = input("Введіть операцію (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Помилка: ділення на нуль!")
                return
            result = num1 / num2
        else:
            print("Невірна операція!")
            return
        
        print(f"Результат: {result}")
    except ValueError:
        print("Помилка: введіть коректні числа!")

# Викликаємо функцію калькулятора
calculator()
