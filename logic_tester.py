a="Welcome"
b="Welcome" 
c="Good-Bye"
d="Good-Bye" 
print(id(a), id(b))
print(c is d)



data=(x*10 for x in range(3)) 
for i in data:
    print(i) 
for j in data:
    print(j)


def wish(message): 
    return lambda name: message.upper() + name
greet = wish(" Happy Birthday ") 
print(greet("Joe"))


def welcome(name): 
    return "Welcome "+name, "Good Bye "+name
wish=welcome("Joe") 
print(wish)


l = [1,2,3,4]

del l[2]
print(l)

