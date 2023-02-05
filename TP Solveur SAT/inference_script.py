from pysat.formula import CNF
from pysat.solvers import Solver
import sys

args = sys.argv

# prendre le fichier depuis lequel on lis notre base de connaissance (.cnf)
base = CNF(from_file=args[1]) 

litteral = int(args[2]) # recuperer notre literal a tester depuis la console directement
litteral_neg = litteral*-1

s = Solver()
for c in base.clauses :
    s.add_clause(c)

s.add_clause([litteral_neg])


# tester si la base infere
if(s.solve()):
    print(f'la base de connaissance n infere pas le literal {litteral}')
else:
    print(f'la base de connaissance infere {litteral}')