import numpy as np
from gates import h_gate, x_gate, iden

def single_gate_operator(n_qubits,gate, t_qubits):
    
    operator = ["i"]*n_qubits
    operator[0] = "u"

    # Swap the U with the target qubit
    operator[0], operator[t_qubits] =  operator[t_qubits], operator[0]
    
    result = iden if operator[0] == "i" else gate
    
    for i in operator[1:]:
        if i == "u":
            result = np.kron(result,gate)
        else:
            result = np.kron(result,iden)
    
    return result

def cnot_operator(n_qubits,t_qubits):

    c_qubit = t_qubits[0]
    t_qubit = t_qubits[1]

    p0x0 = np.array([[1,0],[0,0]])
    p1x1 = np.array([[0,0],[0,1]])

    g1 = g2 = np.array([1])

    for i in range(n_qubits-1):

        if i == c_qubit:
            g1 = np.kron(g1,p0x0)
            g2 = np.kron(g2,p1x1)

        
        if i == t_qubit:
            g1 = np.kron(g1,iden)
            g2 = np.kron(g2,x_gate)
        
        else:
            g1 = np.kron(g1,iden)
            g2 = np.kron(g2,iden)
    

    operator = np.add(g1,g2)

    return operator