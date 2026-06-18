from traffic.RoadSystem import RoadSystem 
from traffic.TrafficLightSystem import TrafficLightSystem
from traffic.TrafficLight import TrafficLight
from traffic.car import Car

class Simulation:
    def __init__(self):
        print("Initialisation de la simulation")
        
        # 1. Instanciation des feux requis avant le TrafficLightSystem
        mbFeu = TrafficLight()
        mtFeu = TrafficLight()
        llFeu = TrafficLight()
        lrFeu = TrafficLight()
        
        # Ajustement des positions visuelles des feux sur le canvas (exemple de disposition)
        mbFeu.x, mbFeu.y = 330, 470
        mtFeu.x, mtFeu.y = 430, 210
        llFeu.x, llFeu.y = 330, 210
        lrFeu.x, lrFeu.y = 430, 470

        self.trafficLightSystem = TrafficLightSystem(mbFeu, mtFeu, llFeu, lrFeu)
        self.roadSystem = RoadSystem()  
        self.cars = []
        
        # Génération de départ
        self.generateRandomly4CarsEachSecondInEachDirection(5)
        
        # Avoir déjà des voitures sur la route au départ
        for i in range(3):
            car = Car()
            car.x = 390
            car.y = i * 150
            self.cars.append(car)

    def generateRandomly4CarsEachSecondInEachDirection(self, numberOfCars): 
        print("Génération aléatoire de", numberOfCars, "voitures par seconde dans chaque direction")
        for i in range(numberOfCars):
            car = Car()
            car.x = 390
            car.y = -(i * 120) - 50
            self.cars.append(car)
            
    def update(self):
        # Déplacement et suppression automatique des voitures hors de l'écran
        for car in self.cars[:]:
            car.move()
            if car.isOutOfScreen():
                self.cars.remove(car)

    # Méthode manquante ajoutée pour l'affichage graphique appelé par gui.py
    def drawCars(self, canvas=None):
        if canvas is not None:
            for car in self.cars:
                canvas.create_rectangle(
                    car.x, 
                    car.y, 
                    car.x + car.width, 
                    car.y + car.height, 
                    fill=car.color,
                    outline="black"
                )