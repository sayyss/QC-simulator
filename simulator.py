import numpy as np
from gates import h_gate,x_gate, iden
from utils import calculate_operator

class Simulator():

    def __init__(self, n_qubits):
        self.n_qubits = n_qubits

        self.s_vector= np.zeros((2**n_qubits), dtype=int)
        self.s_vector[0] = 1
        
    def get_vector(self):
        return self.s_vector
    
    def get_operator(self, gate, t_qubits):
        return

    def single_gate_operator(self,gate,n_qubits, target_qubit):
        
        operator = ["i"]*n_qubits
        operator[0] = "u"
        operator[0], operator[target_qubit] =  operator[target_qubit], operator[0]
        
        result = iden if operator[0] == "i" else gate
        
        for i in operator[1:]:
            if i == "u":
                result = np.kron(result,gate)
            else:
                result = np.kron(result,iden)
        
        return result
    
 
    
