from random import randint

# num = randint(1, 100)

# print()
# print(f'Lucky num: {num}')
# print()

# dice = randint(1,6)
# print()
# print(f'dice felt in: {dice}')
# print()

#============unique ID

# print()
# name = input('enter your first name: ')
# name= name[0:2].upper()
# print()

# lastName = input("Enter your last name: ")
# lastName = lastName[0:2].upper()
# print()

# year = (input('Enter your year of birth: '))
# year = year[2:4]
# print()

# token = str(randint(1000, 9999))

# id= name + token + lastName + year
# print(f'your unique Id: {id}') 

#========Email gen


print()
name = input("Enter your full name: ")
name = name.replace(" ", '.').lower()
print()

enterprise = input("Enter your enterprise name: ")
enterprise = enterprise.replace(" ", ".").lower()
print()
domain = ".com.mx"

email = name + "@" + enterprise + domain

print(f'Yoru new email is: \n\t {email}' )
print()