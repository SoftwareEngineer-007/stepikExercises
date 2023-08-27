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


