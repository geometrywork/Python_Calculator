from kernel import *


print("1 :калькулятор обыкновенный дробей")
print("2 :Калькулятор чисел и десятичных дробей")
choice = int(input("Выберите калькулятор:"))

if choice == 1:
    my_culc = Calc()
    while True:
        print("1: Сложение")
        print("2: Вычитание")
        print("3: Умножение")
        print("4: Деление")
        print("5: Возведение в степень")
        print("6: Exit")
        ch = int(input("Выберите операцию: "))

        #Проверка ввода
        if ch in (1, 2, 3, 4, 5, 6):
            if (ch == 6):
                break
            numerator1 = int(input("Введите числитель первой дроби: "))
            denominator1 = int(input("Введите знаменатель первой дроби: "))
            numerator2 = int(input("Введите числитель второй дроби: "))
            denominator2 = int(input("Введите знаменатель второй дроби: "))
            a = Fraction(numerator1, denominator1)
            b = Fraction(numerator2, denominator2)
            if (ch == 1):
                print(a, "+", b, "=", my_culc.add(a, b))
            elif (ch == 2):
                print(a, "-", b, "=", my_culc.subtract(a, b))
            elif (ch == 3):
                print(a, "*", b, "=", my_culc.multiply(a, b))
            elif (ch == 4):
                print(a, "/", b, "=", my_culc.divide(a, b))
            elif (ch == 5):
                print(a, "**", b, "=", my_culc.degree(a, b))

        else:
            print("Invalid Input")

if choice == 2:
    my_cl = Calculator()
    while True:
        print("1: Сложение")
        print("2: Вычитание")
        print("3: Умножение")
        print("4: Деление")
        print("5: Возведение в степень")
        print("6: Exit")
        ch = int(input("Выберите операцию: "))

        #Проверка ввода
        if ch in (1, 2, 3, 4, 5, 6):

        # Выход из программы
            if (ch == 6):
                break

            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))

            if (ch == 1):
                print(a, "+", b, "=", my_cl.add(a, b))
            elif (ch == 2):
                print(a, "-", b, "=", my_cl.subtract(a, b))
            elif (ch == 3):
                print(a, "*", b, "=", my_cl.multiply(a, b))
            elif (ch == 4):
                print(a, "/", b, "=", my_cl.divide(a, b))
            elif (ch == 5):
                print(a, "**", b, "=", my_cl.degree(a, b))

        else:
            print("Invalid Input")


if __name__ == '__main__':
    main()
