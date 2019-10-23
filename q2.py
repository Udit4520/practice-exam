number = input("Please enter a number :")
number1 = list(number)
numbers = []
for no1 in number1:
    numbers.append(int(no1))
print(sum(numbers))