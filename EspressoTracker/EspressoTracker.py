import csv

def read_file():
    with open("Database/CoffeeList.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        coffee = list(reader)
        return coffee

def find_helper(coffee_list, key_name, key_value):
    matches = [row for row in all_coffee if row[key_name] == key_value]
    return matches

def find_by_brand(coffee_list, brand_name):
    matches = find_helper(coffee_list, 'Brand', brand_name)
    return matches

def find_by_make(coffee_list, make_name):
    matches = find_helper(coffee_list, 'Make', make_name)
    return matches    

all_coffee = read_file()

test_brand = find_by_brand(all_coffee, 'SomeOtherBrand')

for row in test_brand:
    print(row)

test_make = find_by_make(all_coffee, 'SomeMake')

for row in test_make:
    print(row)

with open('Database/CoffeeList.csv', 'a') as csvfile:
    fieldnames = ['Brand', 'Make', 'Roast', 'GrindSize', 'GrindAmount', 'Rating']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'Brand': 'ThirdBrand', 'Make': 'ThirdMake', 'Roast': 'ThirdRoast', 'GrindSize': 7, 'GrindAmount': '3 oclock', 'Rating': 'Gross'})