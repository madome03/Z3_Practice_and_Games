from z3 import *


# model defintion
cur_var = [Bool('a'), Bool('b')]
nxt_var = [Bool('a_x'), Bool('b_x')]
a = cur_var[0]
b = cur_var[1]
a_x = nxt_var[0]
b_x = nxt_var[1]

init_state = And(Not(a), Not(b))
trans_1 = And(And(Not(a), Not(b)), And(Not(a_x), b_x))
trans_2 = And(And(Not(a), Not(b)), And(a_x, Not(b_x)))
trans_3 = And(And(Not(a), b), And(Not(a_x), Not(b_x)))
trans_4 = And(And())


# add other transitions

all_trans = Or(trans_1, trans_2, trans_3)

prop_neg = And(a, b)

#---------------------------------
# BMC encoding for k= 2
bound = 2
new_trans = None

for k in range(1, bound+1): 
    var_k = ['a{}', 'b{}']

    #trans encoding for step 1
    all_trans_k1 = all_trans
    print(k)
    for i in range(len(cur_var)):
        all_trans_k1 = substitute(all_trans_k1, (cur_var[i], Bool(var_k[i].format(k-1))))
    for i in range(len(nxt_var)):
        all_trans_k1 = substitute(all_trans_k1, (nxt_var[i], Bool(var_k[i].format(k))))
    if new_trans is None:
        new_trans = all_trans_k1    
    else:
        new_trans = And(all_trans_k1, new_trans)

print(new_trans)

s = Solver()
s.add(new_trans)
r = s.check()
if r == sat:
    m = s.model()
    print(m)
else:
    print("unsat")