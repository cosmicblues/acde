import names

first_name_list = []
last_name_list = []

for a in range(0, 1001):
    first_name_list.append(names.get_first_name())
    last_name_list.append(names.get_last_name())

print(first_name_list)
print(last_name_list)