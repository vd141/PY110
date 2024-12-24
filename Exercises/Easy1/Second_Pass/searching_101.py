'''
prompt the user for 6 numbers and check if the sixth number is in the first five
'''

numbers_list = []

numbers_list.append((input('Enter the first number: ')))
numbers_list.append((input('Enter the second number: ')))
numbers_list.append((input('Enter the third number: ')))
numbers_list.append((input('Enter the fourth number: ')))
numbers_list.append((input('Enter the fifth number: ')))

numbers_list_str = ','.join(numbers_list)

sixth_number = input('Enter the sixth number: ')

if sixth_number in numbers_list:
    print(f'{sixth_number} is in {numbers_list_str}')
else:
    print(f'{sixth_number} is not in {numbers_list_str}')