name = input("Enter your name: ")
hometown = input("Enter your hometown: ")

age = input("Enter your age: ")
if age.isdigit():
    age = int(age)
else:
    print("Age must be a number")
    exit()

bio = {
    "name": name,
    "hometown": hometown,
    "age": age
}
print(bio["name"], bio["hometown"], bio["age"], sep="\n")