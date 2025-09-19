names = ["sam", "john", "james"]
map_of_names = map(len, names)
print(list(map_of_names))

len_of_names = []
for name in names:
    len_of_names.append(len(name))

print("using loops: ", len_of_names)

list_of_ages = [12, 13, 41, 13, 3, 45, 46]

def verify_age(age):
    return age > 18

age_check = []

for age in list_of_ages:
    check = verify_age(age)
    age_check.append(check)

print(age_check)

map_age = list(map(verify_age, list_of_ages))
print(map_age)

filter = list(filter(verify_age, list_of_ages))
print(filter)

lambda_age = list(map(lambda age: age >= 18, list_of_ages))
print(lambda_age)

show = print

show("hi")

