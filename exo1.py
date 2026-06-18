

color = "red"
width = 20
height = 60
speed = 25 # m/s


def printCar():
    print("Car color:", color)
    print("Car width:", width)
    print("Car height:", height)
    print("Car speed:", speed, "m/s")

def changeSpeed(vitesse):
    global speed
    speed = vitesse
    print("New speed:", speed, "m/s")   


printCar()
changeSpeed(0)
changeSpeed(100)



redLight  = "object avec une couleur rouge vif ou rouge sombre "
greenLight  = "object avec une couleur verte vif ou verte sombre "
yellowLight  = "object avec une couleur jaune vif ou jaune sombre "

greenOrRedTime = 30
yellowTime = 5

def authorizeLight():
    global redLight, greenLight, yellowLight
    greenLight = "mettre une couleur verte vive"
    redLight = "mettre une couleur rouge sombre"
    yellowLight = "mettre une couleur jaune sombre"

    print("Feu vert") 


def stopLight():
    global redLight, greenLight, yellowLight
    greenLight = "mettre une couleur verte sombre"
    redLight = "mettre une couleur rouge vive"
    yellowLight = "mettre une couleur jaune sombre"
    print("Feu rouge")


def cautionLight():
    global redLight, greenLight, yellowLight
    greenLight = "mettre une couleur verte sombre"
    redLight = "mettre une couleur rouge sombre"
    yellowLight = "mettre une couleur jaune vive"

    ## Ici le jaune doit clignoter, 
    # mais pour l'instant on ne peut pas le faire en console, donc on va juste afficher un message
    print("Feu jaune")