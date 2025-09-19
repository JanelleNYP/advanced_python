from functools import reduce


#even and odd numbers

def is_even(num):
    return num%2 == 0

numbers = [1,56,234,87,4,76,24,69,90,135]

even_numbers = []

for number in numbers:
    if is_even(number):
        even_numbers.append(number)

print(even_numbers)

even_numbers_lambda = list(filter(lambda num: num%2 == 0, numbers))
print(even_numbers_lambda)

odd_numbers_lambda = list(filter(lambda num: num%2 == 1, numbers))
print(odd_numbers_lambda)

odd_numbers = list(filter(lambda num: not num%2 == 0, numbers))

print(odd_numbers)


#reduce function

total = reduce(lambda item, running_total: item + running_total, [1, 2, 3, 4, 5])
print(total)


#list comprehensions

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()

length = [len(word) for word in words]
print(length)

not_the = [len(word) for word in words if word != "the"]
print(not_the)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

positive = [number for number in numbers if number >= 0]
print(positive)

numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]

even = [number for number in numbers if numbers if number%2 == 0]
print(even)

words = ["hello", "my", "name", "is", "Sam"]

elements = [(word.upper(), len(word)) for word in words]
print(elements)


