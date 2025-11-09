List1 = ['apple', 'banana', 'mango']

for fruit in List1:
    print(fruit)
    print(f"The length of '{fruit}' is {len(fruit)}")

search = input("Enter fruit name to search: ")

found = False
for fruit in List1:
    if fruit == search:
        print(f"'{search}' is found in the list.")
        found = True
        break

if not found:
    print(f"'{search}' is not found in the list.")