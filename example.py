from simulator import Simulator
from gates import h_gate,x_gate, iden

# Create a quantum "computer" with 3 qubits
simulator = Simulator(3)

# Apply gates
simulator.apply_gate('h',[0])
simulator.apply_gate("cx",[0,1])

# Measure
results = simulator.get_counts(1000)
print(results)