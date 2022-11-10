from z3 import * 


s = Solver()
a0, b0, a1, b1, a2, b2  = Bools('a0 b0 a1 b1 a2 b2')
var = [[a0, b0], [a1, b1], [a2, b2]]

#Initial State
I_S = And(Not(var[0][0]), (Not(var[0][1])))
#Left State
S_L = And(Not(var[1][0]), var[1][1])
#Right State
S_R = And(var[1][0], Not(var[1][1]))
#Bottom State
S_B = And(var[2][0], var[2][1])
K_0 = And(I_S, S_L, I_S)
K_1 = And(I_S, S_R, I_S)
K_2 = And(I_S, S_R, S_B)
K_3 = Or(S_B, S_B, S_B)
Final_Model = And(Or(K_0, K_1, K_2), K_3)
s.add(Final_Model)
r = s.check()
if r == sat:
    m = s.model()
    print(m)
else:
    print("unsat")