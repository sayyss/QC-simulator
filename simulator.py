import numpy as np
from gates import h_gate,x_gate, iden, cnot,p0x0,p1x1
import random

class Simulator():

    def __init__(self, n_qubits):
        self.n_qubits = n_qubits

        self.s_vector= np.zeros((2**n_qubits), dtype=int)
        self.s_vector[0] = 1
        
    def get_state(self):
        return self.s_vector
    
    def apply_gate(self,gate,t_qubits):

        if self.n_qubits > 1:
            self.s_vector = np.dot(self.s_vector, self.get_operator(gate, t_qubits))

        else:
            self.s_vector = np.dot(self.s_vector, gate)
        
        return self.s_vector

    def get_operator(self, gate, t_qubits):

        if gate == "cx":
            return self.cnot_operator(gate,t_qubits)
        else:
            return self.single_gate_operator(gate, t_qubits)

    def single_gate_operator(self,gate, t_qubits):
        
        operator = ["i"]*self.n_qubits
        operator[0] = "u"
        operator[0], operator[t_qubits] =  operator[t_qubits], operator[0]
        
        result = iden if operator[0] == "i" else gate
        
        for i in operator[1:]:
            if i == "u":
                result = np.kron(result,gate)
            else:
                result = np.kron(result,iden)
        
        return result

    def cnot_operator(self,gate,t_qubits):

        c_qubit = t_qubits[0]
        t_qubit = t_qubits[1]

        temp_p0x0, temp_p1x1 = p0x0,p1x1
        g_1 = g_2 = np.array([1])

        for i in range(self.n_qubits-1):

            if i == c_qubit:
                g_1 = np.kron(g_1,temp_p0x0)
                g_2 = np.kron(g_2,temp_p1x1)
 
            
            if i == t_qubit:
                g_1 = np.kron(g_1,iden)
                g_2 = np.kron(g_2,x_gate)
            
            else:
                g_1 = np.kron(g_1,iden)
                g_2 = np.kron(g_2,iden)
        

        operator = np.add(g_1,g_2)
        print(np.shape(operator))
        print(np.shape(self.s_vector))
        return operator
        
    def measure(self):

        prob = np.abs(self.s_vector)**2
        indexes = np.arange(np.size(self.s_vector))

        measure = random.choices(indexes, weights=prob, k=1)

        return bin(measure[0])
    
    def get_counts(self,n_shots):
        
        result = {}

        for i in range(n_shots):
            measure = self.measure()

            if measure in result:
                result[measure] += 1
            
            else:
                result[measure] = 1
        
        return result

pc = Simulator(2)

pc.apply_gate(h_gate,0)
pc.apply_gate("cx",[0,1])

print(pc.get_counts(1000))


