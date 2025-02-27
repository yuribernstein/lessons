import json

class BankAccount():
    def __init__(self, first_name, last_name, currency):
        self.bank_account = {
        'currency': currency,
        'balance': 0,
        'account_holder': {
            'first_name': first_name,
            'last_name': last_name
            }
        }        

    def deposit(self, amount):
        self.bank_account['balance'] += int(amount)

    def withdraw(self, amount):
        if amount > self.bank_account['balance']:
            print('Insufficient funds')
        else:
            self.bank_account['balance'] -= int(amount)

    def dump_to_file(self):
        with open('account.json', 'w') as f:
            json.dump(f, self.bank_account)







        








# def numbers_operation(num1, num2, operation):
#     if operation == '+':
#         result = num1 + num2
#     elif operation == '-':
#         result = num1 - num2
#     else:
#         result = 'Operation is not valid'
#     return result

# number_1 = int(input('Provide fist number: '))
# number_2 = int(input('Provide second number: '))
# my_operation = input('Provide operation: ')
# print(numbers_operation(number_1, number_2, my_operation))



# def greeting(greet, name, additional_greet='Good to see you'):
#     return f'{greet} {name}, {additional_greet}'



# function_response = greeting('Hello and Welcome', 'Daniel')
# print(function_response)


