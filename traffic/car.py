import random

class Car:
    def __init__(self, color=None, width=None, height=None, speed=None, crossRoadChangeDirection=None):
        self.initializeRandomyCar()
        # Supprimé : self.move() pour éviter d'avancer avant le premier cycle d'affichage
        self.x = 390
        self.y = 0
        self.canvasObject = None

    def removeCar(self):
        print("Removing the car from the simulation...")

    def initializeRandomyCar(self):
        self.color = random.choice(["red", "blue", "green", "yellow", "black"])
        self.width = random.randint(15, 20)
        self.height = random.randint(30, 40)
        self.speed = random.randint(2, 6)
        self.crossRoadChangeDirection = random.choice(["straight", "left", "right"])
        self.direction = random.choice(["up", "down", "left", "right"])

    def printCar(self):
        print("Car color:", self.color)
        print("Car width:", self.width)
        print("Car height:", self.height)
        print("Car speed:", self.speed, "m/s")

    def move(self):
        # Déplace la voiture vers le bas
        self.y += self.speed
        print("The car is moving at a speed of", self.speed, "m/s")

    def changeSpeed(self, vitesse):
        self.speed = vitesse
        print("New speed:", self.speed, "m/s")
    
    def turn(self, direction):
        if direction.lower() == "left":
            self.direction = "left"
            print("Turning left...")
        elif direction.lower() == "right":
            self.direction = "right"
            print("Turning right...")
        else:
            print("Invalid direction. Please specify 'left' or 'right'.")
    
    def changeDirection(self):
        # Correction pour ne pas écraser le nom de la méthode
        self.current_direction = self.crossRoadChangeDirection
        print("Changing direction to:", self.crossRoadChangeDirection)

    def lidar(self):
        print("Scanning the environment...")

    # Méthode ajoutée pour permettre la suppression en dehors de l'écran
    def isOutOfScreen(self):
        if self.y > 800 or self.y < -100 or self.x > 800 or self.x < -100:
            return True
        return False