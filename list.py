# Problem I want to input number and print average of it

#step 1 first ask user to input how many number they want to input
#step 2 taking a number of input base on number of input recieve from user

# number_input = int(input("Number of input"))

# temp = 1
# final_number = 0

# while temp <= number_input:
#     number = float(input("Enter your number"))
#     final_number += number
#     temp += 1

# print(final_number/number_input)


input_number = input("Enter list of number")
convert_to_list = input_number.split(" ")

final = 0
for num in convert_to_list:
    final += int(num)

print(final/len(convert_to_list))