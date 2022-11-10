from z3 import *
#Page 11 BMC slide


s = Solver()
t = Solver()
l = Solver()
d = Solver()
Counter = Solver()
a0, b0, a1, b1, a2, b2= Bools('a0 b0 a1 b1 a2 b2')

#k0 Model  
k0 = And(And(Not(a0, b0)), And(a0, b0))  
s.add(k0)
r = s.check()    
if r == sat:
    m = s.model()
    print(m)
else:
    print("unsat")


#k1 Model
k1 = Or(And(And(Not(a0, b0), And(Not(a1), b1)), (And(Not(a0, b0), a1, Not(b1))), And(a0, b0), Or(And(a1,b1)))) 
t.add(k1)
q = t.check()
if q == sat:
    o = t.model()
    print("Sat")
else:
    print("unsat")



#K2 Model
k2 = And(Not(a0, b0), Not(a1), b1, Not(a2, b2)), Or(And(Not(a0, b0), a1, Not(b1, a2), Not(b2))), And(a0, b0), Or(And(a1, b1),Or(And(a2, b2)))
l.add(k2)
p = l.check()    
if p == sat:
    j = l.model()
    print(j)
else:
    print("unsat")


#K3 Satisfiable Model
k3 = And(Or(Or(And(Not(a0, b0), Not(a1), b1, Not(a2, b2)), Or(And(Not(a0, b0), a1, Not(b1, a2), Not(b2))), And(Not(a0, b0), a1, Not(b1), a2,b2), And(a0, b0), Or(And(a1, b1), Or(And(a2, b2))))))
d.add(k3)
D = d.check()
if D == sat:
    w = d.model()
    print("sat" + "-" + str(w))
else:
    print("unsat")

#Counter - Example
C_O = And(Not(a0, b0), a1, Not(b1), a2, b2)
Counter.add(C_O)
C = Counter.check()
if C == sat:
    c = Counter.model()
    print("Counter example" + str(c))
else:
    print("unsat")



