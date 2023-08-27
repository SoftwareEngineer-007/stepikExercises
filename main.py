# 1 Lesson topic: data input-output

print('Hello, World!')


print('What is you name?')
name = input()
print('Hi,', name)


another_name = input('Input you name: ')
print('Hello,', another_name)
print('Nice to meet you ;)')

# 2 Lesson topic: sep, end, variables, PEP 8

# Напишите программу, которая выводит на экран текст «I***like***Python» (без кавычек).
print('I', 'like', 'Python', sep='***')

# Напишите программу, которая считывает строку-разделитель и три строки, а затем выводит указанные строки через разделитель.
sepor = input('Input sep: ')
line1 = input('Input line 1: ')
line2 = input('Input line 2: ')
line3 = input('Input line 3: ')
print(line1, line2, line3, sep=sepor)

# Напишите программу, которая приветствует пользователя, выводя слово «Привет» (без кавычек), после которого должна стоять запятая и пробел, а затем введенное имя и восклицательный знак.
name = input('Input your name: ')
print('Привет, ', name, sep='', end='!')


# 3 Lesson topic: Integer arithmetic

# Напишите программу вывода на экран трех последовательно идущих чисел, каждое на отдельной строке. Первое число вводит пользователь, остальные числа вычисляются в программе.
num = int(input('Input int num: '))
print(num)
print(num + 1)
print(num + 2)

# Напишите программу, которая считывает три целых числа и выводит на экран их сумму. Каждое число записано в отдельной строке.
num1 = int(input())
num2 = int(input())
num3 = int(input())
sum = num1 + num2 + num3
print(sum)

# Напишите программу, вычисляющую объём куба и площадь его полной поверхности, по введённому значению длины ребра.
length = int(input('Введите длину ребра куба: '))
v = length ** 3
s = 6 * (length ** 2)
print('Объем =', v)
print('Площадь полной поверхности =', s)

# Напишите программу вычисления значения функции f(a,b)
a = int(input())
b = int(input())
f = 3*((a+b)**3)+275*(b**2)-127*a-41
print(f)

# Напишите программу, которая считывает целое число, после чего на экран выводится следующее и предыдущее целое число с пояснительным текстом.
num1 = int(input())
num0 = num1 - 1
num2 = num1 + 1
print('Следующее за числом', num1, 'число:', num2)
print('Для числа', num1, 'предыдущее число:', num0)

# Напишите программу, которая считывает целое положительное число x и выводит на экран последовательность чисел x,2x,3x,4x и 5x, разделённых тремя черточками.
x = int(input())
print(x, x*2, x*3, x*4, x*5, sep='---')

# 4 Lesson topic: working with integers

# Геометрическая прогрессия
b1 = int(input())
q = int(input())
n = int(input())
b = b1 * q ** (n-1)
print(b)

# n школьников делят k мандаринов поровну, неделящийся остаток остается в корзине. Сколько целых мандаринов достанется каждому школьнику? Сколько целых мандаринов останется в корзине?
schoolboy = int(input())
orange = int(input())
to_every_schoolboy = orange // schoolboy
in_basket = orange % schoolboy
print(to_every_schoolboy)
print(in_basket)

# Безумный титан Танос собрал все 6 камней бесконечности и намеревается уничтожить половину населения Вселенной по щелчку пальцев. При этом если население Вселенной является нечетным числом, то титан проявит милосердие и округлит количество выживших в большую сторону. Помогите Мстителям подсчитать количество выживших.
population = int(input())
remainder = population % 2
survivors = (population // 2) + remainder
print(survivors)

# В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом. Напишите программу, которая определяет номер купе, в котором находится место с заданным номером (нумерация мест сквозная, начинается с 1)
place_number = int(input())
compartment_number = (place_number + 3) // 4
print(compartment_number)

# Напишите программу для пересчёта величины временного интервала, заданного в минутах, в величину, выраженную в часах и минутах.
minutes = int(input())
hour = minutes // 60
minute = minutes - (hour * 60)
print(minutes, 'мин - это', hour, 'час', minute, 'минут.')

# Программа получения цифр двузначного числа
num = 17
a = num % 10
b = num // 10
print(a)  # 7
print(b)  # 1

# Программа получения цифр трёхзначного числа
num = 754
a = num % 10
b = (num % 100) // 10
c = num // 100
print(a)  # 4
print(b)  # 5
print(c)  # 7

# Напишите программу, определяющую число десятков и единиц в двузначном числе
num = int(input())
last_digit = num % 10
first_digit = num // 10
print('Число десятков =', first_digit)
print('Число единиц =', last_digit)

# Напишите программу, в которую вводится трёхзначное число и которая выводит на экран его цифры (через запятую)
num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100
print(digit1, digit2, digit3, sep=',')

# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.
num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100
print('Сумма цифр =', digit1 + digit2 + digit3)
print('Произведение цифр =', digit1 * digit2 * digit3)

# Дано трехзначное число abc, в котором все цифры различны. Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа. (abc,acb,bac,bca,cab,cba)
num = int(input())
digit_c = num % 10
digit_b = (num // 10) % 10
digit_a = num // 100
print(digit_a, digit_b, digit_c, sep='')
print(digit_a, digit_c, digit_b, sep='')
print(digit_b, digit_a, digit_c, sep='')
print(digit_b, digit_c, digit_a, sep='')
print(digit_c, digit_a, digit_b, sep='')
print(digit_c, digit_b, digit_a, sep='')

# Напишите программу для нахождения цифр четырёхзначного числа.
num = int(input())
digit_units = num % 10
digit_tens = (num // 10) % 10
digit_hundreds = (num // 100) % 10
digit_thousand = num // 1000
print('Цифра в позиции тысяч равна', digit_thousand)
print('Цифра в позиции сотен равна', digit_hundreds)
print('Цифра в позиции десятков равна', digit_tens)
print('Цифра в позиции единиц равна', digit_units)


