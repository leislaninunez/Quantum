from qiskit import QuantumCircuit
from qiskit.providers.aer import AerSimulator
from qiskit.visualization import plot_histogram

simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

from qiskit import QuantumCircuit
from qiskit.providers.aer import AerSimulator
from qiskit.visualization import plot_histogram

# Create 8-qubit quantum circuit
qc = QuantumCircuit(8, 8)

# Ry angles: Dravet high firing, ATS low firing
ry_angles = [2.0, 2.0, 2.0, 2.0, 0.785, 0.785, 0.785, 0.785]

for i, angle in enumerate(ry_angles):
    qc.ry(angle, i)

# Linear CNOT chain
for i in range(7):
    qc.cx(i, i+1)

# Measure all qubits
qc.measure(range(8), range(8))

# Run simulation
sim = AerSimulator()
result = sim.run(qc, shots=1024).result()
counts = result.get_counts()
plot_histogram(counts)