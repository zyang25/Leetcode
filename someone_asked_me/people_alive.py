# the most people alive

class Person:
    
    def __init__(self, birth, death):
        self.birth = birth
        self.death = death

p1 = Person(1991, 2060)
p2 = Person(1998, 2191)
p3 = Person(2001, 2020)
p4 = Person(2009, 2031)
p5 = Person(2010, 2030)
p6 = Person(2025, 2070)
p7 = Person(2035, 2080)

l = list()
l.append(p1)
l.append(p2)
l.append(p3)
l.append(p4)
l.append(p5)
l.append(p6)
l.append(p7)

prev = l[0]
count = 0
min_birth = l[len(l)-1].birth
max_death = l[len(l)-1].death

for i in range(1, len(l)):
    curr = l[i]
    # overlap
    if curr.birth < prev.death:
        count += 1
        if curr.birth < min_birth:
            min_birth = curr.birth

print(count, min_birth)