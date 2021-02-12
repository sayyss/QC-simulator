import numpy as np

# Identity Matrix
iden = np.identity(2)

# X(NOT) gate
x_gate = np.array([[0, 1],
              [1, 0]])

# Hadamard gate
h_gate = np.array([[1/np.sqrt(2), 1/np.sqrt(2)],
              [1/np.sqrt(2), -1/np.sqrt(2)]])

# CNOT gate

cnot = np.array([[1,0,0,0],
                [0,1,0,0],
                [0,0,0,1],
                [0,0,1,0]])
# Projection gatse
p0x0 = np.array([[1,0],[0,0]])
p1x1 = np.array([[0,0],[0,1]])
