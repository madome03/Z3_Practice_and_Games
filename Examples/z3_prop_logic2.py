from z3 import*

"""
If it is snowing and I dont have my jacket I will get cold
If I have my jacket I will not get cold
"""
"""
S - snwoing
J - jacket with him
C - Cold
"""

S, J, C = Bools('S, J, C')

s = Solver()

s.add(Implies(And(S, Not(J)), C))


s.add(Not(C))

s.add(S)

s.add(J)

r = s.check()
m = s.model()

if r == sat:

    print(m)
else:
    print("unsat")

