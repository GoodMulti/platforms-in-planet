from objects import Earth

from simulation import Simulation

from visualize import Show

def showSimulation():
    
    aSim = Simulation(Earth('Home'))

    return Show(aSim)


