numbers = input("Enter a list of numbers separated by spaces: ")

num = [float(num) for num in numbers.split()]

if num:
    smallest_number = min(num)
    largest_number = max(num)

    print(" smallest number :", smallest_number)
    print(" largest number :", largest_number)
else:
    print(" Please enter some numbers.")