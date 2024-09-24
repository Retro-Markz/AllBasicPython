print()

# name = str(input('Enter your name: '))
# age = int(input('Enter your age: '))
# heigh = float(input('Enter your heigh: '))

# print(f'\nWellcome: {name}, {age}, {heigh}')



#------EMPLOYEE SYSTEM

# print()
# full_name = str(input("enter your name: "))

# employeeName = full_name.replace(" ", '').lower().strip()

# age = int(input("Enter the employee Age: "))

# salary = float(input('Enter employee Montly Salary: '))

# isChief = bool(input("is the employee a department Chief? (True/False): "))

# print()
# employe_data = f"The Employee Name is: {employeeName}, \nhe/She is {age} years old, \nthe aprooved pay per month is: ${salary} USD, \nthe Employee chief status is: {isChief}"

# print(employe_data)
# print()


#------- RECIPE 


print("**** Recipe ****")
print()

recipeName = str(input("Recipe Name: "))
recipeName = recipeName.upper()

print()

ingridients = []
for i in range(10):
     element = input("give some ingredients, separate them with comma: ")
     ingridients.append(element)
     break

ingr = ', '.join(ingridients)
print()

time = int(input("how many minutes it take to prepare? "))

print()

difficult = input("how difficult it\'s to prepare? (easy, normal, hard)")
dif = ''.join(difficult)
exp = dif.replace(' ','')

print()

print('*** Now you know how to do ***')
print()
print(f'\t{recipeName}. \n\nyou will need: {ingr}.\nIt will take you {time} minutes to prepare \nand it\'s {exp} to do')

