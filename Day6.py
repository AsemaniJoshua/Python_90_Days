# Day 6: Lists and Tuples
# - Topics:
# - Learn about lists and tuples: how to create, access, modify, and delete elements.
# - List methods: append(), remove(), pop().
# - Project:
# - Create a program that takes a list of numbers and prints the sum and average.

userlist = input("Enter a list of numbers separated by a comma(\",\"): \n").split(",")
userlist = [int(i) for i in userlist]
sum_of_numbers = 0
average_of_numbers = 0
counter = 0

def print_sum_and_average(userlist, sum_of_numbers, counter, average_of_numbers):
    for i in userlist:
        sum_of_numbers += i
        counter += 1
    print(f"Sum of numbers: {sum_of_numbers}")
    average_of_numbers = sum_of_numbers / counter
    print(f"Average of numbers: {average_of_numbers}")

print_sum_and_average(userlist, sum_of_numbers, counter, average_of_numbers)

# def print_average(userlist, sum_of_numbers, counter):
#     for i in userlist:
#         sum_of_numbers += i
#         counter += 1
#     average_of_numbers = sum_of_numbers / counter
#     print(f"Average of numbers: {average_of_numbers}")


