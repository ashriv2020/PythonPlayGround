listname = [1,2,3,4,5]

total = sum(listname)

print(total)
total_times = int(input('Enter loop number'))
listname = []
for m in range(total_times):
    user_choice = int(input('Enter number'))
    listname.append(user_choice)

total_of_entered_numbers = sum(listname)
print(f'Total of entered numbers: {total_of_entered_numbers}')