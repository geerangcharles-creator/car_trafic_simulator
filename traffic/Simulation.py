from traffic import RoadSystem 
from traffic.TrafficLightSystem import TrafficLightSystem
from traffic.car import Car


class Simulation:
    def __init__(self):
        print("Initialisation de la simulation")
        self.trafficLightSystem = TrafficLightSystem()
        self.roadSystem = RoadSystem()  
        self.cars=[]
        self.generateRandomly4CarsEachSecondInEachDirection(5)# Génération aléatoire de 5 voitures par seconde dans chaque direction
        
        #avoir deja des voiture sur la route 
        for i in range(5):
            
            car = Car(None, None, None, None, None)
            car.x = 390
            car.y = i * 100
            self.cars.append(car)

    


    def generateRandomly4CarsEachSecondInEachDirection(self, numberOfCars): 
        print("Génération aléatoire de", numberOfCars, "voitures par seconde dans chaque direction")
        # un algo pour générer aléatoirement des voitures dans chaque direction
        for i in range(numberOfCars):
            car = Car(None, None, None, None, None)
            car.x = 390
            car.y = -(i * 50)
            self.cars.append(car)
         
    #tkinter fera appelle a ca    
    def update(self):
    #suppression de voiture
        for car in self.cars[:]:
            car.move()
            if car.isOutOfScreen():
                self.cars.remove(car)
    
    #methode pour dessiner
    def drawCars(self, canvas):
     for car in self.cars:
            car.draw(canvas)