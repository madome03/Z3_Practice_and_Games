from z3 import *
from Stated_Trans import T as t

class BMC(object):
    #---------------------------------
    # BMC encoding for k=2
    def __init__(self):
        pass

    @staticmethod
    def full_trans():
        data = t.Trans_Combined()
        bound = 2
        new_trans = None
        for k in range(1, bound+1): 
            var_k = ['a{}', 'b{}']
            #trans encoding for step 1
            all_trans_k1 = data 
            for i in range(len(t.cur_var)):
                all_trans_k1 = substitute(all_trans_k1, (t.cur_var[i], Bool(var_k[i].format(k-1))))
            for i in range(len(t.nxt_var)):
                all_trans_k1 = substitute(all_trans_k1, (t.nxt_var[i], Bool(var_k[i].format(k))))
            if new_trans is None:
                new_trans = all_trans_k1    
            else:
                new_trans = And(all_trans_k1, new_trans)
        return new_trans
    @staticmethod
    def z3_solver(full_trans):
        s = Solver()
        s.add(full_trans)
        r = s.check()
        if r == sat:
            m = s.model()
            print("sat", m, end="")
        else:
            print("unsat")

Transition = BMC()
Transition.z3_solver(Transition.full_trans())

                    

