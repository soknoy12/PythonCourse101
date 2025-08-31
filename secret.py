secret = 33
num = 0

while num != secret:
    num = int(input("Guess the number"))
    if num < secret:
        print("It too low")
    elif num > secret:
        print("It too high")
    else:
        print("Yayy, you are correct")
        print("The secret number is", secret)