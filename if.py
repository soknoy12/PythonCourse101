
age = int(input("Enter your age"))


if age >= 2 and age < 13:
    print("Kid")
elif age <= 1 and age >= 0:
    if age == 0:
        month = int(input("How many month you were born"))
        if month >= 0:
            print("Valid month")
        else:
            print("Invalid month")
    print("Infant")
elif age >= 13 and age < 19:
    print("Teeneger")
elif age >= 19 and age < 22:
    print("Adult")
elif age >= 22:
    print("Chill Guy")
else:
    print("Invalid")