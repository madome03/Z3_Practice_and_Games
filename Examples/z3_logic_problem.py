from re import I
from z3 import*

"""
There are 100 politicians
at least one is honest
for any two at least one is crooked
How many honest politicians are there?
"""

politicians = [Bool('x % s' % i)for i in range(100)]

atleastonehonest = Or(politicians)


#finally and all the clauses together
atleast2crooked = And([Or(Not(i), Not(j)) for i in politicians for j in politicians if not i is j])

smth = solve(atleastonehonest, atleast2crooked)

s = Solver()

s.add(atleastonehonest, atleast2crooked)

print(s.check())
solution = s.model()
print(solution)
