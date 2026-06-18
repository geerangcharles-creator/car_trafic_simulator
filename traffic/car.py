import random

class Car:
    def __init__(self, color, width, height, speed, crossRoadChangeDirection):
        self.initializeRandomyCar()
        self.move()
        #ajout de x et y pour dessine les objet a une position
        self.x=0
        self.y=0
        self.canvasObject= None



    def removeCar(self):
        print("Removing the car from the simulation...")

    def initializeRandomyCar(self):
        self.color = random.choice(["red", "blue", "green", "yellow", "black"])
        self.width = random.randint(1, 2)
        self.height = random.randint(1, 2)
        self.speed = random.randint(10, 30)
        self.crossRoadChangeDirection = random.choice(["straight", "left", "right"])
        #ajout de la direction
        self.direction = random.choice(["up", "down", "left", "right"])
        


    def printCar(self):
        print("Car color:", self.color)
        print("Car width:", self.width)
        print("Car height:", self.height)
        print("Car speed:", self.speed, "m/s")

    def move(self):
        #la mise ajour qui deplace la voiture
        self.y += 5
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
        self.changeDirection= self.crossRoadChangeDirection
        print("Changing direction to:", self.crossRoadChangeDirection)
        


    def lidar(self):
        # This function simulates the LIDAR sensor of the car, which scans the environment 
        # and detects obstacles.
        print("Scanning the environment with LIDAR...  ")
        
    #fonction qui supprime la voiture de la simulation
    def isOutOfScreen(self):

        if self.y > 800:
         return True

        return False
