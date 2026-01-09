names = ["Jake", "Zac", "Ian", "Sam", "Dave"]

search = input("Enter name to search: ")

if search in names:
    print(search, "found in the list")
else:
    print(search, "not found")
