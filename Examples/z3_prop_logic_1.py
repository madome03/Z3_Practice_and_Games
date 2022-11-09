from z3 import*

"""
If it is raining and Jane does not have her umbrella with her she will
get wet. Jane is not wet, It is raining therefore Jane has her Umbrella 
with her
"""
"""
R = Raining 
U = Umbrella with her
W = Wet
"""
R, U, W = Bools('R, U, W')

s = Solver()

#Implies Raining and no umbrella means Wet
s.add(Implies(And(R, Not(U)), W))

#Jane is not Wet
s.add(Not(W))

#It is raining
s.add(R)

#Jane has her Umbrella
s.add(U)

r = s.check()
m = s.model()

if r == sat:
    
    print(m)
else:
    print("unsat")