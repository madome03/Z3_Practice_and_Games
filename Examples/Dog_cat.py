from z3 import*

"""
Consider the following puzzle. Spend exactly 100 dollars and buy exactly 100 animals. 
Dogs cost 15 dollars, cats cost 1 dollar, and mice cost 25 cents each. 
You have to buy at least one of each. How many of each should you buy?
"""

Dogs, Cats, Mice = Ints('Dogs Cats Mice')

s = Solver()

#Dogs, Cats, Mice summed equal 100
s.add(Dogs + Cats + Mice == 100)
s.add(Dogs*15 + Cats*1 + Mice*.25 == 100)
s.add(Dogs >= 1)
s.add(Cats >= 1)
s.add(Mice >= 1)

r = s.check()
m = s.model()

if r == sat:
    print(m)
else:
    print("unsat")
