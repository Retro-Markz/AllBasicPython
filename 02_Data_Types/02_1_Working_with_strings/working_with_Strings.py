
#special characters

print()

a = 'it\'s a new day'

print(a)
print()

b = 'in the new message \\ just select the backslash'

print(b)
print()

c = 'it\'s easy when you practice, \nand everybody need to practice'

print(c)
print()

d = 'well let\'s see what\'s  \r  a carrierbarrier does'
print(d)
print()

e = '\t adding a tab is easy \nthe best part it\'s to apply it'
print(e)
print()

a = "what\'s a \bBackspace? \nreally don\'t know"
print(a)
print()

a = 'form feed \f seem\'s new to me\n\tlet\'s try it'
print(a)
print()

a = '''let\'s try form feed\f
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse efficitur ipsum sit amet ex vestibulum finibus. Praesent eu placerat quam. Ut pellentesque vestibulum orci, ac interdum dolor ornare id. Mauris posuere mollis lacus eget vestibulum. Mauris finibus augue id ante accumsan, et sollicitudin purus aliquet. Maecenas rhoncus vulputate urna, vel suscipit diam varius vitae. Donec molestie lacus et imperdiet faucibus. Donec eu porta elit. Nam bibendum dui urna, vitae tempor purus egestas a. Donec tempus volutpat lorem, vel venenatis sapien fermentum nec. Pellentesque eu venenatis est, quis ornare velit. Proin eget magna ac sapien dapibus convallis finibus quis turpis. Integer justo lacus, aliquam at hendrerit eget, feugiat et nunc.
'''

print(a)
print()


#String functions

#join()

a = 'hello'
b = 'world'
res = a + " " +  b 
print(res)


concat = "".join([a, ' ', b])
print(concat)

#format

res = f'hello {b}'
print(res)

name = 'Mark'
age = 37

dev = f'hi, i\'m {name} and i\'m {age} years old'
print(dev)

 #upper()
 
var1 = "hello mates"
 
print(f'original var: {var1}')
 
upperVar = var1.upper()
 
print(f'Upper the var: {upperVar}')

#lower()
lowerVar = var1.lower()

print(f'Upper the var: {lowerVar}')

#strip()

spacedVar = " hello Mates "
print(f'spaced string: {spacedVar}')
print(f'space removed string: {spacedVar.strip()}')

