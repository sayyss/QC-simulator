import numpy as np
import random
from gates import h_gate, x_gate, iden
from utils import cnot_operator, single_gate_operator

class Simulator():

    # Gates
    gates = {
        "h": h_gate,
        "x": x_gate,
        "cx": None
    }

    # Initialize simulator with n_qubits
    def __init__(self, n_qubits):
        self.n_qubits = n_qubits

        self.s_vector= np.zeros((2**n_qubits), dtype=int)
        self.s_vector[0] = 1
        
    def get_state(self):
        return self.s_vector
    
    def apply_gate(self,gate,t_qubits):

        if gate not in self.gates:
            raise KeyError("Gate not found")

        if gate == "cx":
            if self.n_qubits < 2:
                raise TypeError("CNOT gate cannot be applied on 2 > qubit simulator")

            else:
                self.s_vector = np.dot(self.s_vector, self.get_operator(gate, t_qubits))
        
        else:
            if self.n_qubits > 1:
                self.s_vector = np.dot(self.s_vector, self.get_operator(gate,t_qubits))
            else:
                self.s_vector = np.dot(self.s_vector,self.gates[gate])
                
        return self.s_vector

    def get_operator(self, gate, t_qubits):

        if gate == "cx":
            return cnot_operator(self.n_qubits, t_qubits)
        else:
            return single_gate_operator(self.n_qubits,self.gates[gate], t_qubits)

    def measure(self):

        prob = np.abs(self.s_vector)**2

        # All the possible outputs
        indexes = np.arange(np.size(self.s_vector))

        # Weighted random 
        measure = random.choices(indexes, weights=prob, k=1)

        # Return the qubit index in binary
        return bin(measure[0])
    
    # Runs measure() n_shots time
    def get_counts(self,n_shots):
        
        result = {}

        for i in range(n_shots):
            measure = self.measure()

            if measure in result:
                result[measure] += 1
            
            else:
                result[measure] = 1
        
        return result


