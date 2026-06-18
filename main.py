from traffic.Simulation import Simulation
from traffic.gui import GUI


simulation = Simulation()

gui = GUI(simulation)

gui.run()