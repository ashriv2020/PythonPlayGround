menus = [[ 'Egg Sandwich', 'Bagel', 'Coffee'],
         ['BLT', 'Veg Sandwich', 'Tea'],
         ['Panner', 'Chhas', 'Curd']]

print(menus[0][1])   

menus2 = {'Breakfast':[ 'Egg Sandwich', 'Bagel', 'Coffee'],
         'Lunch':['BLT', 'Veg Sandwich', 'Tea'],
         'Dinner':['Panner', 'Chhas', 'Curd']}

print(menus2['Breakfast'])

for name, menu in menus2.items():
    print(name, ':', menu)

person = {
    'name': 'Abhishek',
    'Age': 24,
    'City': 'Mumbai'

}  
print(person)
print(person.get('name'), ' is ' , person.get('Age'), ' years old and lives in ', person.get('City')) 