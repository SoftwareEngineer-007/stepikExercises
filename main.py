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

#Напишите программу, которая приветствует пользователя, выводя слово «Привет» (без кавычек), после которого должна стоять запятая и пробел, а затем введенное имя и восклицательный знак.
name = input('Input your name: ')
print('Привет, ', name, sep='', end='!')

