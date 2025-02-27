
##TARGIL 4 - CHECK FOR NEGATIVE NUMBER
number = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
if number < 0 and number2 < 0:
    print("Both numbers are negative")
elif number < 0 or number2 < 0:
    print("One of the numbers is negative")
else:
    print("both numbers are positive")

###TARGIL 5 - REVERSE THE NUMBERS
number_1 = input("Enter a number: ")
print("The reverse number is: ", number_1[::-1])

###TARGIL 6 - TAX CALCULATION
salary = int(input("Enter your salary: "))
tax = input("Enter your tax percentage: ")
tax = int(tax) / 100
print(f"Your total salary after tax is {salary-(salary * tax)}")

###TARGIL 7 -  CM TO M 
cm = float(input("Enter the length in cm: "))
print(f"The length in meters is: {cm / 100} meters")

###TARGIL 8 -  CHECK IF STRING IS INSIDE OTHER STRING
string1 = input("Enter a string: ")
string2 = input("Enter another string: ")
if  string2 in string1:
    print("The first string is inside the second string")
else:
    print("The first string is not inside the second string")

###TARGIL 9 -  AMOUNT OF MONEY IN BANKNOTES
amout_of_cash = float(input("Enter the amount of money: "))
print(f"Number of 200 notes: {int(amout_of_cash / 200)}")
print(f"Number of 100 notes: {int(amout_of_cash % 200 / 100)}")
print(f"Number of 50 notes: {int(amout_of_cash % 200 % 100 / 50)}")
print(f"Number of 20 notes: {int(amout_of_cash % 200 % 100 % 50 / 20)}")
print(f"Number of 10 coins: {int(amout_of_cash % 200 % 100 % 50 % 20 / 10)}")
print(f"Number of 5 coins: {int(amout_of_cash % 200 % 100 % 50 % 20 % 10 / 5)}")
print(f"Number of 1 coins: {int(amout_of_cash % 200 % 100 % 50 % 20 % 10 % 5 / 1)}")


#TARGIL 10 - COUNTDOWN
number = int(input("Enter a number: "))
for i in range(number, -1, -1):
    print(i)


#TARGIL 11 - FIBONACCI SERIES
a, b = 0, 1
for i in range(10):
    print(a)
    a, b = b, a + b

#TARGIL 12 -  CHECK LIST
fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
user_input = input("Enter a fruit: ")
if user_input in fruits:
    print("you like the same fruits as me")
else:
    print("you don't like the same fruits as me")


#TARGIL 13 -  ADD ITEMS TO A LIST
movies_list = []
movies_list.append(input("the first the movie: "))
movies_list.append(input("the second the movie: "))
movies_list.append(input("the third the movie: "))
for i in movies_list:
    print(f"your favorites movie is {i}")

#TARGIL 14 - SUM USER INPUT
def sum_numbers(numbers): #why the fuck i need numbers in this function???
    return sum(numbers)

user_numbers = []

for i in range(5):
    number = int(input(f"Enter number #{i+1}: "))
    user_numbers.append(number)

result = sum_numbers(user_numbers)
print(f"The sum of your numbers is: {result}.")
