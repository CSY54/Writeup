from z3 import *

X = [ [ Int("x_%s_%s" % (i+1, j+1)) for j in range(9) ]
      for i in range(9) ]

# each cell contains a value in {1, ..., 9}
cells_c  = [ And(1 <= X[i][j], X[i][j] <= 9)
             for i in range(9) for j in range(9) ]

# each row contains a digit at most once
rows_c   = [ Distinct(X[i]) for i in range(9) ]

# each column contains a digit at most once
cols_c   = [ Distinct([ X[i][j] for i in range(9) ])
             for j in range(9) ]

# each 3x3 square contains a digit at most once
sq_c     = [ Distinct([ X[3*i0 + i][3*j0 + j]
                        for i in range(3) for j in range(3) ])
             for i0 in range(3) for j0 in range(3) ]

sudoku_c = cells_c + rows_c + cols_c + sq_c

# sudoku instance, we use '0' for empty cells
instance = (
    (1,0,0,0,6,0,8,5,0),
    (0,0,5,0,8,3,1,0,0),
    (0,0,0,0,1,2,0,9,0),
    (9,0,7,0,0,0,0,0,0),
    (5,3,0,0,0,0,0,8,9),
    (0,0,0,0,0,0,3,0,5),
    (0,4,0,6,2,0,0,0,0),
    (0,0,6,1,9,0,7,0,0),
    (0,2,1,0,3,0,0,0,4),
)

instance_c = [ If(instance[i][j] == 0,
                  True,
                  X[i][j] == instance[i][j])
               for i in range(9) for j in range(9) ]

s = Solver()
s.add(sudoku_c + instance_c)
if s.check() == sat:
    m = s.model()
    r = [ [ m.evaluate(X[i][j]) for j in range(9) ]
          for i in range(9) ]
    print_matrix(r)
else:
    print "failed to solve"

'''
[[1, 7, 2, 4, 6, 9, 8, 5, 3],
 [4, 9, 5, 7, 8, 3, 1, 2, 6],
 [6, 8, 3, 5, 1, 2, 4, 9, 7],
 [9, 6, 7, 3, 5, 8, 2, 4, 1],
 [5, 3, 4, 2, 7, 1, 6, 8, 9],
 [2, 1, 8, 9, 4, 6, 3, 7, 5],
 [3, 4, 9, 6, 2, 7, 5, 1, 8],
 [8, 5, 6, 1, 9, 4, 7, 3, 2],
 [7, 2, 1, 8, 3, 5, 9, 6, 4]]
'''
