from z3 import *

#The puzzles contraints
"""
There are  5 houses in five different colours. 
In each house lives a person with a different nationality.
These five owners drink a certain type of beverage, smoke a certain brand of cigar and keep a certain pet.
No owners have the same pet, smoke the same brand of cigar or drink the same beverage.
The Brit lives in the red house.
The swede keeps dogs as pets.
The dane drinks tea.
The green house is on the left of the white house.
The green house owner drinks coffee.
The person who smokes pallmall rears birds.
The owner of the yellow house smokes dunhill.
The man living in the centre house drinks milk.
The Norwegian lives in the first house.
The man who smokes blends lives next to the one who keeps cats.
The man who keeps horses lives next to the man who smokes dunhill.
The owner who smokes bluemaster drinks beer.
The German smokes prince.
The Norwegian lives next to the blue house.
The man who smokes blends has a neighbour who drinks water.
Who owns the fish?
"""

#create z3 variables for each attribute
house, nat, col, pet, cig, bev = [0,1,2,3,4,5]
houses = {0:"House1", 1:"House2", 2:"House3", 3:"House4", 4:"House5"}

#create z3 varibales for each color on the houses
red, blue, green, yellow, white = [0,1,2,3,4]
colors = {red:"Red", blue: "Blue", green:"Green", yellow:"Yellow", white:"White"}

#create z3 variables for each nationality
brit, swede, dane, german, norwegian = [0,1,2,3,4]
nationality = {brit:"Brit", swede:"Swede", dane:"Dane", german:"German", norwegian:"Norw"}

#create z3 variables for each prt
fish, cat, bird, dog, horse = [0,1,2,3,4]
pets = {fish:"Fish", cat:"Cat", bird:"Bird", dog:"Dog", horse:"Horse"}

#create z3 variables for each beverage
pallmall, dunhill, bluemaster, blends, prince = [0,1,2,3,4]
cigars = {pallmall:"Pallmall", dunhill:"Dunhill", bluemaster:"Bluemaster", blends:"Blends", prince:"Prince"}

#create z3 for each drink
milk, tea, coffee, beer, water = [0,1,2,3,4]
bevs = {milk:"Milk", tea:"Tea", coffee:"Coffee", beer:"Beer", water:"Water"}

columns = {house:houses, nat:nationality, col:colors, pet:pets, cig:cigars, bev:bevs}

def Abs(x):
    return If(x >=0, x, -x)

class AssignmentPuzzleSolver:
    def __init__(self):
        self.X = [[Int("x_%s_%s" % (i, j)) for j in range(6)]
                      for i in range(5)]
        self.s = Solver()
        self.s.add([And(0 <= self.X[i][j], self.X[i][j]<= 4) 
                    for i in range(5) for j in range(6)])

    def set_constraints(self):
        cons = []
        
        # there is no repetition along each dimension
        cols_c = [Distinct([self.X[i][j] for i in range(5)]) for j in range(6)]
        cons.append(And(cols_c))

        # The brit lives in the red house
        cons1 = Or([And(self.X[i][nat] == brit, self.X[i][col] == red) 
                        for i in range(5)])
        cons.append(cons1)

        # The swede keeps dogs as pets
        cons2 = Or([And(self.X[i][nat] == swede, self.X[i][pet] == dog)
                            for i in range(5)])
        cons.append(cons2)
        
        # The dane drinks tea
        cons3 = Or([And(self.X[i][nat] == dane, self.X[i][bev] == tea)
                            for i in range(5)])
        cons.append(cons3)
        
        # The green house is on the left of the  white house
        cons4 = []
        for i in range(4):
            for j in range(i+1,5):
                cons4.append(And(self.X[i][col] == green, self.X[j][col] == white))
        cons4 = Or(cons4)
        cons.append(cons4)
        
        # The green house owner drinks coffee
        cons5 = Or([And(self.X[i][col] == green, self.X[i][bev] == coffee)
                            for i in range(5)])
        cons.append(cons5)
        
        # The person who smokes pallmall rears birds
        cons6 = Or([And(self.X[i][cig] == pallmall, self.X[i][pet] == bird)
                            for i in range(5)])
        cons.append(cons6)
        
        # The owner of the yellow house smokes dunhill
        cons7 = Or([And(self.X[i][col] == yellow, self.X[i][cig] == dunhill)
                            for i in range(5)])
        cons.append(cons7)
        
        # The man living in the centre house drinks milk
        cons8 = Or([And(self.X[i][house] == 2, self.X[i][bev] == milk)
                            for i in range(5)])
        cons.append(cons8)
        
        # The Norwegian lives in the first house
        cons9 = Or([And(self.X[i][nat] == norwegian, self.X[i][house] == 0)
                        for i in range(5)])
        cons.append(cons9)
        
        # The man who smokes blends lives next to the one who keeps cats
        cons10 = []
        for i in range(5):
            for j in range(5):
                if i != j:
                    cons10.append(And(self.X[i][cig] == blends, self.X[j][pet] == cat,
                        Abs(self.X[i][house]-self.X[j][house]) == 1))
        cons10 = Or(cons10)
        cons.append(cons10)
        
        # The man who keeps horses lives next to the man who smokes dunhill
        cons11 = []
        for i in range(5):
            for j in range(5):
                if i != j:
                    cons11.append(And(self.X[i][pet] == horse, self.X[j][cig] == dunhill,
                                          Abs(self.X[i][house]-self.X[j][house]) == 1))
        cons11 = Or(cons11)
        cons.append(cons11)
        
        # The owner who smokes bluemaster drinks beer
        cons12 = Or([And(self.X[i][cig] == bluemaster,self.X[i][bev] == beer)
                            for i in range(5)])
        cons.append(cons12)
        
        # The german smokes prince
        cons13 = Or([And(self.X[i][nat] == german, self.X[i][cig] == prince)
                            for i in range(5)])
        cons.append(cons13)
        
        # The Norwegian lives next to the blue house
        cons14 = Or([And(self.X[i][house] == 1, self.X[i][col] == blue)
                            for i in range(5)])
        cons.append(cons14)
        
        # The man who smokes blends has a neighbour who drinks water
        cons15 = []
        for i in range(5):
            for j in range(5):
                if i != j:
                    cons15.append(And(self.X[i][cig] == blends, self.X[j][bev] == water,
                                Abs(self.X[i][house]-self.X[j][house]) == 1))
        cons15 = Or(cons15)
        cons.append(cons15)
        
        self.s.add(And(cons))

    #create output solution
    def output_solution(self):
        m = self.s.model()
        print("\t".join(["House","Nationality","Colour","Pets","Cigars","Beverages"]))
        for i in range(5):
            print("\t".join([columns[j][m.evaluate(self.X[i][j]).as_long()] for j in range(6)]))

    #check for sat the
    def solve(self):
        self.set_constraints()
        if self.s.check() == sat:
            self.output_solution()
        else:
            print(self.s)
            print("Failed to solve.")

s = AssignmentPuzzleSolver()
s.solve()
