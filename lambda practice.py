#lambda practice that I've done. Feel free to use for your own practice


#Simple Operations:
print('#Write a lambda function that takes a number and returns its square.')
Q1 = list(map(lambda x: x **2,range(1,11)))
print(Q1)
print('--------------------------')

print('#Write a lambda function that takes two numbers and returns their product.')
x = [1,2,3,4,5]
y = [6,4,2,7,1]
equasion = lambda x,y: x * y
mapped_eq = list(map(equasion,x,y))
print(mapped_eq)
print('--------------------------')


#List Operations:
print('#Given a list of strings, use a lambda function to sort the list by the length of the strings.')
string_list = ["apple", "banana", "kiwi", "orange"]
sorted_lst = list(sorted(string_list, key=lambda x: len(x)))
print(sorted_lst)
print('--------------------------')

print('#Use map() and a lambda function to convert a list of temperatures from Celsius to Fahrenheit.')
x = None

far_lst = [90, 70, 120, 110]
cel_lst = [0, 35, 15, -20]

conv_c2f = list(map(lambda x: round((x * 9/5) + 32,2), cel_lst))
conv_f2c = list(map(lambda x: round((x - 32) * 5/9,2), far_lst))
print(f'original list of Fahrenheit that is then converted to Celsius: \n{far_lst}\nConverted values: \n{conv_c2f}\n')
print(f'original list of Celsius that is then converted to Fahrenheit: \n{cel_lst}\nConverted values: \n{conv_f2c}')
print('--------------------------')


#Filtering Data:
print('#Use filter() and a lambda function to filter out odd numbers from a list.')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fil_numbs = list(filter(lambda x: x % 2 == 0,numbers))
print(fil_numbs)
print('--------------------------')

print('#Given a list of tuples (name, age), use filter() and a lambda function to filter out people younger than 18.\n')
print('''starting code: \n
people = [("Alice", 22), ("Bob", 17), ("Charlie", 19), ("Diana", 15), ("Edward", 20)]''')

people = [("Alice", 22), ("Bob", 17), ("Charlie", 19), ("Diana", 15), ("Edward", 20)]
filt_ppl = list(filter(lambda person: person[1] >= 18,people))
filt_ppl_names = list(map(lambda person: person[0],filt_ppl))
print(filt_ppl_names)
print('--------------------------')


#Advanced Sorting:
print('#Given a list of dictionaries representing students with name and grade, use a lambda function to sort the list by grade.\n')
print('''starting code: \n
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "David", "grade": 88},
    {"name": "Eva", "grade": 95}
]
''')

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "David", "grade": 88},
    {"name": "Eva", "grade": 95}
]

sorted_stu = sorted(students, key=lambda student:student['grade'])
sorted_stu_names = list(map(lambda stud: stud['name'],sorted_stu))
print(f'result: sorted_stu_names')
print('--------------------------')


print('#Sort a list of tuples by the second element in descending order using a lambda function.\n')
print(''' starting code: \n
products = [
    ("Laptop", 999.99),
    ("Smartphone", 499.99),
    ("Headphones", 89.99),
    ("Monitor", 199.99),
    ("Keyboard", 29.99),
    ("Mouse", 19.99),
    ("Webcam", 59.99)
]
''')

products = [
    ("Laptop", 999.99),
    ("Smartphone", 499.99),
    ("Headphones", 89.99),
    ("Monitor", 199.99),
    ("Keyboard", 29.99),
    ("Mouse", 19.99),
    ("Webcam", 59.99)
]

srt_products = sorted(products, key=lambda price:price[1], reverse=True)
srt_products_names = list(map(lambda name:name[0],srt_products))
print(f'result: {srt_products_names}')























