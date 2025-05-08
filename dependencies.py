#funções criadas por Yuri3358

def simple_calc(a, b): #Exercício 01-06
    if type(a) and type(b) == int:
        print(f"Soma: {a + b} \n Produto: {a * b} \n Potência {a ** b}")
        if a == 0 or b == 0:
            print("Resultado ausente, impossível divisão por zero")
        else:
            print(f"Divisão: {a / b} \n Divisão Inteira: {a // b} \n Resto: {a % b}")
    else:
        print("Erro de tipagem")

def average(n1, n2, n3): #exercício 07
    print((n1 + n2 + n3) / 3)

def retangular_perimeter(base, height): #exercício 08
    print(2*(base*height))

def area_calc(b, h, op): #exercícios 08, 10
    try:
        if op == "tr":
            print(b*h/2)
        elif op == "rt":
            print(b*h)
    except TypeError:
        print("Erro de tipagem!!")

def temperature_converter(celsius, unit): #exercícios 11-12 e 10 da lista 2
    if unit == "f":
        converted_unit = celsius * 9/ 5 + 32
        unit = "ºF"
    elif unit == "k":
        converted_unit = celsius + 273.15
        unit = "K"

    print(f"{celsius}°C -> {converted_unit}{unit}")

def time_converter(time_in_hours): #exercício 13
    print(f"Tempo em minutos: {time_in_hours*60} \n Tempo em segundos {time_in_hours*3600}")

def average_speed(km, h): #exercício 14
    print(f"{km / h}km/h")

def bmi_calc(height, weight): #exercício 15
    print(f"O seu IMC é {weight / height ** 2}")

def values_changer(n1, n2): #exercício 16
    a = n1 + n2
    b = n1 - n2
    a = b
    b = a
    print(f"Valor de a: {a} \n Valor de b: {b}")

def string_mixer(str_a, str_b): #exercício 17
    print(str_a+str_b)

def string_lenght(text): #exercício 18
    print(len(text))

def type_converter(value): #exercício 19
    if type(value) == int:
        print(float(value))

def digits_sum(n): #exercício 20
    str_n = str(n)
    if len(str_n) == 3:
        print(int(str_n[0]) + int(str_n[1]) + int(str_n[2]))

# All functions below are from the second list
def rule_checker(number): #exercício 1
    if number > 0:
        print("Positivo")
    elif number < 0:
        print("Negativo")
    else: 
        print("Zero")

def odd_or_even(number): #exercício 2
    if number % 2 == 0:
        print("Par!")
    else:
        print("Ímpar")

def biggest_number(amount): #exercícios 3-4 (l2)
    array = []
    for value in range (0, amount):
        number = int(input(f"Digite o {value+1}º valor: "))
        array.append(number)
    print(sorted(array)[-1])

def range_checker(number, a, b): #exercício 5
    range_list = range(a, b)
    if number in range_list:
        print(f"{number} pertence ao intervalo [{a}, {b}]")
    else:
        print(f"{number} não pertence ao intervalo")

#exercício 6
def leap_year_checker(year):
    if year % 4 == 0 or year % 100 == 0 and year % 400 == 0:
        print("Ano bissexto!") 

#exercícios 7-8
def score_checker(grade):
    if grade >= 0 and grade <= 10:
        if grade > 7:
            print("Aprovado")
        elif grade >= 5 and grade <= 7:
            print("Recuperaçação")
        elif grade < 5:
            print("Reprovado")

#exercício 09
def progressive_discount(transaction_value):
    if transaction_value >= 1000:
        print(transaction_value - transaction_value*0.10)
    elif transaction_value > 500 and transaction_value < 1000:
        print(transaction_value - transaction_value*0.05)
    elif transaction_value <= 500:
        print(transaction_value)

#exercício 11
def login_system(username, password):
    if username == "John Doe" and password == "itsmypassword123":
        print("Login autorizado!")
    else:
        print("Acesso negado")

#exercício 12
def vowel_or_consonant_checker(letter):
    if letter in "AEIOUaeiou":
        print("Vogal detectada!")
    else:
        print("Consoante")

#exercício 13
def age_categories(age: int):
    if age < 13:
        print("Criança")

    elif age < 18 and age >= 13:
        print("Adolescente")
    
    elif age <= 60 and age >= 18:
        print("Adulto")
    
    else: 
        print("Idoso")

#exercício 14
def transport_ticket(age):
    if age <= 6:
        print("Grátis")
    elif age < 18 and age > 6:
        print("Meia")
    elif age >= 18:
        print("Inteira")

#exercício 15
def money_loan(monthly_wage, loan_value, age):
    if monthly_wage >= loan_value / 3 and age in range(21, 65):
        print("Aprovado")
    else:
        print("Reprovado")

#exercício 16
def divide_checker(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0 and number % 5 != 0:
        print("Fizz")
    elif number % 5 == 0 and number % 3 != 0:
        print("Buzz")
    else:
        print(number)

#exercício 17
def withdrawal(credit, withdrawal_value):
    if credit <= withdrawal_value and withdrawal_value % 10 == 0:
        print("Saque autorizado")
    else:
        print("Negado!!")

## lista 03

def list_numbers(n): #exercício 01
    for i in range(0, n):
        print(i)

def sum_numbers(n): #exercício 02
    counter = 0
    for i in range(0, n+1):
        counter += i
    print(counter)

def number_factorial(n): #exercício 03
    result = 1
    for i in range(1, n+1):
        result *= i
    print(result)

def numbers_generator(n, n_filter): #exercícios 4-5
    numbers_list = []
    for i in range(0, n+1):
        if n_filter == "even":
            if i % 2 == 0:
                numbers_list.append(i)
        elif n_filter == "odd":
            if i % 2 != 0:
                numbers_list.append(i)
    return numbers_list

def sum_numbers(n, n_filter): #exercícios 6-7

    counter = 0
    for i in numbers_generator(n, n_filter):
        counter += i
    print(counter)

def times_table(target_number): #exercício 8
    for i in range(0, 10+1):
        print(f"{i} x {target_number} = {i*target_number}")

def countdown(start_number): #exercício 09
    while start_number >= 0:
        start_number -= 1
        print(start_number+1)

def powered_numbers(number, exponent): #exercícios 10-12
    for i in range(0, number+1):
        print(i**exponent)

def string_length(word: str): #exercício 13
    counter = 0
    for char in word:
        counter += 1
    print(counter)

def vowel_counter(word): #exercício 14
    counter = 0
    for letter in word:
        if letter in "AEIOUaeiou":
            counter += 1
    print(counter)

def sum_digits(number: int): #exercício 15
    pass

def prime_checker(number): #exercício 16
    for i in range (2, number-1):
        if i % 2 != 0:
            print("It's prime")
        else:
            print("It's not prime")
            
def divisors_counter(target_number): #exercício 17
    divisors_list = []
    for number in range(1, target_number+1):
        if target_number % number == 0:
            divisors_list.append(number)
    print(divisors_list)

def sum_numbers_loop(): #exercício 18
    counter = 0
    number = 1
    while number != 0:
        number = int(input("Digite um número: "))
        counter += number
    print(counter)

def asterisk_pyramid(number: int, inverted: bool = False): #exercício 19-20
    if inverted == False:
        for amount in range(1, number+1):
            print("*"*amount)
    elif inverted == True:
        for amount in reversed(range(1, number+1)):
            print("*"*amount)