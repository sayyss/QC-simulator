import numpy as np
from gates import h_gate,x_gate

class Simulator():


    def __init__(self, n_qubits):
        self.n_qubits = n_qubits

        self.s_vector= np.zeros((2**n_qubits), dtype=int)
        self.s_vector[0] = 1
        
    def get_vector(self):
        return self.s_vector
    
    def get_operator(self, gate, t_qubits):

        if n_qubits == 1:
            
            if gate == "h_gate":
                return h_gate
            
            if gate == "x_gate":
                return x_gate
        
        


    
