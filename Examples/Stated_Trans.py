from z3 import *
class T(object):
    #Initializing the Model Definition  
    def __init__(self):        
        pass
    cur_var = [Bool('a'), Bool('b')] 
    nxt_var = [Bool('a_x'), Bool('b_x')]
    a = cur_var[0]
    b = cur_var[1]
    a_x = nxt_var[0]
    b_x = nxt_var[1]
    @staticmethod
    def Trans_Combined():
        init_state = And(Not(T.a), Not(T.b))
        trans_1 = And(And(Not(T.a), Not(T.b)), And(Not(T.a_x), T.b_x))
        trans_2 = And(And(Not(T.a), Not(T.b)), And(T.a_x, Not(T.b_x)))
        trans_3 = And(And(Not(T.a), T.b), And(Not(T.a_x), Not(T.b_x)))
        trans_4 = And(And(T.a, Not(T.b)), And(Not(T.a_x), Not(T.b_x)))
        prop_neg = And(T.a, T.b)
        trans_5 = And(And(T.a, Not(T.b)), prop_neg)
        trans_6 = And(prop_neg, init_state)
        # add other transitions 
        all_trans = Or(trans_1, trans_2, trans_3, trans_4, trans_5,)
        return all_trans 
