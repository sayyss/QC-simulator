import numpy as np
from gates import h_gate,x_gate

def calculate_operator(gate, t_qubits, n_qubits):
    
    if gate == "h_gate":
        i = np.identity(2)
        operator = np.kron(np.kron(i,i),h_gate)
        