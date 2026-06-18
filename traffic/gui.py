import tkinter as tk


class GUI:

    def __init__(self, simulation):

        self.simulation = simulation

        self.root = tk.Tk()

        self.root.title("Traffic Simulation")

        self.canvas = tk.Canvas(
            self.root,
            width=800,
            height=800,
            bg="white"
        )

        self.canvas.pack()

    def update(self):

        self.canvas.delete("all")

        self.simulation.roadSystem.drawRoads(
            self.canvas
        )

        self.simulation.trafficLightSystem.drawTrafficLights(
            self.canvas
        )

        self.simulation.update()

        self.simulation.drawCars(
            self.canvas
        )

        self.root.after(
            50,
            self.update
        )

    def run(self):

        self.update()

        self.root.mainloop()