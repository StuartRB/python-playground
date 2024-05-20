# variables
age = 28
is_sleepy = True

# user input
name = input("What is your name? ")
print("Hello ", name, ". Sleepy indicator: ", is_sleepy)
birth_year = input("What is your year off birth? ")
age = 2024 - int(birth_year)
print("Age: ", age)

# type conversion
first = input("First: ")
second = input("Second: ")
sum = float(first) + float(second)
print("Result: " + str(sum))

# string methods
course = "python for losers"
print(course.upper())
print(course.find("for"))
print(course.replace("losers", "legends"))
print("losers" in course)  # returns boolean

# arithmetic operators
print("sum:", 10 + 1)
print("s§ubtract:", 10 - 1)
print("multiply:", 10 * 1)
print("divide:", 10 / 3)  # returns float
print("floor division:", 10 // 3)  # returns int
print("modulus:", 10 % 3)  # modulus (remainder)
print("exponent:", 10 ** 3)  # exponent
x = 10
x += 3  # augmented assignment operator
print(x)

is_stu_legend = True
print("Stu is a legend: " + str(is_stu_legend and x > 10))
print("Les is a legend: " + str(not (is_stu_legend and x > 10)))

if is_stu_legend:
    print("Yes he is")
elif x < 23:
    print("Madness!")
else:
    print("I dunno then")

count = 1
while count < 10:
    print(count * "*")
    count = count + 1

names = ["Robert", "Susan", "Maisie", "Harry"]
print(names)
print(names[1])  # second in list
print(names[-2])  # second last in list
names[-1] = "Busterson"
print(names)
print(names[0:3])  # 1st, 2nd and 4rd
maisie_moo = names.index("Maisie")
print(names[0:maisie_moo])  # print everything in the list before 'Maisie'

numbers = [1, 2, 3, 4, 5]
numbers.insert(len(numbers), 6)
print(numbers)
print(2 in numbers)  # True or False

for item in numbers:
    print(item)

print()

other_numbers = range(6)
for number in other_numbers:
    print(number)

print()

other_numbers = range(5, 100, 5)
for number in other_numbers:
    print(number)

print(" # tuples")

numbers = (1, 2, 3, 3)  # immutable
print(numbers)

"cock".casefold()