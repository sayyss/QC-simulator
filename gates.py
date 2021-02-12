import numpy as np

# Identity Matrix
iden = np.identity(2)

# X(NOT) gate
x_gate = np.array([[0, 1],
              [1, 0]])

# Hadamard gate
h_gate = np.array([[1/np.sqrt(2), 1/np.sqrt(2)],
              [1/np.sqrt(2), -1/np.sqrt(2)]])
