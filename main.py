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

# ЭКЗАМЕН

#Напишите программу, которая выводит прямоугольник, по периметру состоящий из звездочек (*). Примечание. Высота и ширина прямоугольника равны 4 и 17 звёздочкам соответственно.
print(17 * "*")
print("*", "*", sep=15 * " ")
print("*", "*", sep=15 * " ")
print(17 * "*")

# Напишите программу, которая считывает два целых числа a и b и выводит на экран квадрат суммы и сумму квадратов этих чисел.
a = int(input())
b = int(input())
z = (a + b) ** 2
x = (a ** 2) + (b ** 2)
print('Квадрат суммы', a, 'и', b, 'равен', z)
print('Сумма квадратов', a, 'и', b, 'равна', x)

# Как известно, целые числа в языке Python не имеют ограничений, которые встречаются в других языках программирования. Напишите программу, которая считывает четыре целых положительных числа a,b,c и d и выводит на экран значение выражения
a = int(input())
b = int(input())
c = int(input())
d = int(input())
z = (a ** b) + (c ** d)
print(z)

# Напишите программу, которая считывает целое положительное число n,n∈[1;9] и выводит значение числа n+nn+nnn
a = int(input())
z = a + (a * 11) + (a * 111)
print(z)

# 4 Условный оператор

# Напишите программу, которая считывает три числа и подсчитывает количество чётных чисел.
num1, num2, num3 = int(input()), int(input()), int(input())
counter = 0  # переменная счётчик
if num1 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num2 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num3 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
print(counter)

# При регистрации на сайтах требуется вводить пароль дважды. Это сделано для безопасности, поскольку такой подход уменьшает возможность неверного ввода пароля. Напишите программу, которая сравнивает пароль и его подтверждение. Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».
pass1 = input()
pass2 = input()
if pass1 == pass2:
    print('Пароль принят')
else:
    print('Пароль не принят')

# Напишите программу, которая определяет, является число четным или нечетным.
num = int(input())
if num % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

# Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение: сумма первой и последней цифр равна разности второй и третьей цифр.
num = int(input())
fourth_num = num % 10
third_num = (num // 10) % 10
second_num = (num // 100) % 10
first_num = num // 1000
if (first_num + fourth_num) == (second_num - third_num):
    print('ДА')
else:
    print('НЕТ')

# Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными членами арифметической прогрессии.
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num3 - num2 == num2 - num1:
    print('YES')
else:
    print('NO')

# Напишите программу, которая определяет наименьшее из двух чисел.
num1 = int(input())
num2 = int(input())
if num1 > num2:
    print(num2)
else:
    print(num1)

# Напишите программу, которая определяет наименьшее из четырёх чисел.
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
if num1 > num2:
    num12 = num2
else:
    num12 = num1
if num3 > num4:
    num34 = num4
else:
    num34 = num3
if num12 > num34:
    print(num34)
else:
    print(num12)

# Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:
# до 13 включительно – детство;
# от 14 до 24 – молодость;
# от 25 до 59 – зрелость;
# от 60 – старость.
age = int(input())
if age <= 13:
    print('детство')
if 14 <= age <= 24:
    print('молодость')
if 25 <= age <= 59:
    print('зрелость')
if age >= 60:
    print('старость')

# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 >= 0:
    num1 = num1
else:
    num1 = 0
if num2 >= 0:
    num2 = num2
else:
    num2 = 0
if num3 >= 0:
    num3 = num3
else:
    num3 = 0
print(num1 + num2 + num3)

# Напишите программу, которая проверяет, что все три цифры натурального трёхзначного числа различны.
num = int(input())
d3 = num % 10
d2 = num % 100 // 10
d1 = num // 100
if d3 != d2 and d3 != d1 and d2 != d1:
    print('Цифры различны')
else:
    print('Цифры не различны')

# Напишите программу, которая по координатам точки, не лежащей на осях координат, определяет номер координатной четверти, в которой она находится.
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1 четверть')
if x < 0 and y > 0:
    print('2 четверть')
if x < 0 and y < 0:
    print('3 четверть')
if x > 0 and y < 0:
    print('4 четверть')

# Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам.
num = int(input())
if num <= -3 or num >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')

num = int(input())
if -30 < num <= -2 or 7 < num <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')

# Назовем число красивым, если оно является четырехзначным и делится нацело на 7 или на 17. Напишите программу, определяющую, является ли введённое число красивым. Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.
num = int(input())
if (num % 7 == 0 or num % 17 == 0) and 1000 <= num <= 9999:
    print('YES')
else:
    print('NO')

# Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник с такими сторонами.
a = int(input())
b = int(input())
c = int(input())
if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    print('YES')
else:
    print('NO')

#Напишите программу, которая определяет, является ли год с данным номером високосным. Если год является високосным, то выведите «YES», иначе выведите «NO».
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or year % 400 == 0:
    print('YES')
else:
    print('NO')

# Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли ладья попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до
# 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом ладьи можно попасть во вторую, или «NO» в противном случае.
column_out = int(input())
line_out = int(input())
column_in = int(input())
line_in = int(input())
if (1 <= column_out <= 8 and column_out == column_in) or (1 <= line_out <= 8 and line_out == line_in):
    print('YES')
else:
    print('NO')

#Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли король попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом короля можно попасть во вторую, или «NO» в противном случае.
column_out = int(input())
line_out = int(input())
column_in = int(input())
line_in = int(input())
if (column_out <= column_in + 1 and column_out >= column_in - 1) and (line_out <= line_in + 1 and line_out >= line_in - 1):
    print('YES')
else:
    print('NO')

# Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).
# 1 способ. Использование вложенного условного оператора.
a, b, c = int(input()), int(input()), int(input())

if a == b:
    if b == c:
        print(3)
    else:
        print(2)
else:
    if a == c:
        print(2)
    else:
        if b == c:
            print(2)
        else:
            print(0)

# 2 способ. Использование каскадного условного оператора.
a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print(3)
elif a == b != c:
    print(2)
elif a != b == c:
    print(2)
elif a == c != b:
    print(2)
else:
    print(0)

# 3 способ. Использование каскадного условного оператора и логического оператора or.
a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print(3)
elif a == b != c or a != b == c or a == c != b:
    print(2)
else:
    print(0)

# Зум бросил вызов Флэшу и предложил ему честный поединок в виде гонки вокруг магнетара. В случае проигрыша эта нейтронная звезда зарядится и уничтожит мир, поэтому Флэш решил не рисковать без причины и узнать у своего друга Циско Рамона, есть ли смысл принимать вызов. Циско получил данные, что скорость Зума равна n, а скорость Флэша равна k.
n_z = int(input())
k_f = int(input())
if n_z > k_f:
    print('NO')
elif n_z < k_f:
    print('YES')
else:
    print("Don't know")

# Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам.
a = int(input())
b = int(input())
c = int(input())
if a != b and a != c and b != c:
    print('Разносторонний')
elif a == b == c:
    print('Равносторонний')
else:
    print('Равнобедренный')

# Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.
a = int(input())
b = int(input())
c = int(input())
if a > b > c or c > b > a:
    print(b)
elif c > a > b or b > a > c:
    print(a)
else:
    print(c)

# Дан порядковый номер месяца (1,2,…, 12). Напишите программу, которая выводит на экран количество дней в этом месяце. Принять, что год является невисокосным.
month = int(input())
if month == 2:
    print('28')
elif month == 4 or month == 6 or month == 9 or month == 11:
    print('30')
else:
    print('31')

# Известен вес боксера-любителя (целое число). Известно, что вес таков, что боксер может быть отнесён к одной из трех весовых категорий:
# Легкий вес – до 60 кг;
# Первый полусредний вес – до 64 кг;
# Полусредний вес – до 69 кг.
# Напишите программу, определяющую, в какой категории будет выступать данный боксер.
weight = int(input())
if 69 > weight >= 64:
    print('Полусредний вес')
elif 64 > weight >= 60:
    print('Первый полусредний вес')
else:
    print('Легкий вес')

# Напишите программу, которая считывает с клавиатуры два целых числа и строку. Если эта строка является обозначением одной из четырёх математических операций (+, -, *, /), то выведите результат применения этой операции к введённым ранее числам, в противном случае выведите «Неверная операция». Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!».
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
act = input('Что необходимо сделать? (+, -, *, /): ')
if num2 == 0 and act == '/':
    print('На ноль делить нельзя!')
elif act == '+':
    print(num1 + num2)
elif act == '-':
    print(num1 - num2)
elif act == '*':
    print(num1 * num2)
elif act == '/':
    print(num1 / num2)
else:
    print('Неверная операция')
