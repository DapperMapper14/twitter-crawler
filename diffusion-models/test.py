import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from gillespie import SI_Simulation # Import the model.

G = nx.erdos_renyi_graph(1000,0.05) # Use Networkx to generate a random graph.

model = SI_Simulation(G, lam=0.8, gam=0.001, i0=0.0) # Setup the simulation with given parameters.
model.RunToConvergence() # Run the simulation.
model.IntegrateSolution() # Numerically integrate the mean field equations.

# Simulation.
plt.plot(model.times,model.S/model.N, 'g-', label='Susceptible (sim)')
plt.plot(model.times,model.I/model.N, 'r-', label='Infected (sim)')

# Numerical Integration.
t = np.linspace(0,model.times[-1],100)
plt.plot(t, model.solution[:,0],'g--', label='Susceptible (approx)')
plt.plot(t, model.solution[:,1],'r--', label='Infected  (approx)')

plt.xlabel('t')
plt.ylabel('Population Fraction')

plt.legend(bbox_to_anchor=(1.0,0.7))
plt.show()