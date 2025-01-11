# Find Maximum from rows and minimum from columns 
# a=([[15,20,25,30,40],[16,36,32,19,40],[45,92,72,56,65],[67,47,87,27,37],[50,60,65,55,85]])
# o/p: [40,40,92,87,85]
# o/p: [15,20,25,19,37]

import numpy as np
a = np.array([[15,20,25,30,40],[16,36,32,19,40],[45,92,72,56,65],[67,47,87,27,37],[50,60,65,55,85]])

max_rows = np.max(a, axis=1)  # Maximum from each row
min_columns = np.min(a, axis=0)  # Minimum from each column

print(max_rows)
print(min_columns)
