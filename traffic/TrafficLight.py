class TrafficLight:
    greenOrRedTime = 30
    yellowTime = 5

    def __init__(self, redLight, greenLight, yellowLight):
        self.__color = "Red"
        self.redLight = redLight
        self.greenLight = greenLight
        self.yellowLight = yellowLight
        self.x= 500
        self.y= 300

    

    def drawLight(self,canvas=None):
        print("Affichage du feu de circulation")
        print("Couleur du feu : ", self.__color)
        print("Durée du feu vert : ", self.greenOrRedTime, " secondes")
        print("Durée du feu rouge : ", self.greenOrRedTime, " secondes")
        print("Durée du feu jaune : ", self.yellowTime, " secondes")
        
        if canvas is not None:
            canvas.create_rectangle(
                self.x,
                self.y,
                self.x +40,
                self.y +120,
                fill="black"
            )
            canvas.create_oval(
                self.x + 10,
                self.y + 10,
                self.x + 30,
                self.y + 30,
                fill=self.redLight
            )
            canvas.create_oval(
                 self.x + 10,
                 self.y + 50,
                 self.x + 30,
                 self.y + 70,
                 fill=self.yellowLight
            )
            canvas.create_oval(
                self.x + 10,
                self.y + 90,
                self.x + 30,
                self.y + 110,
                fill=self.greenLight
            )


    def authorizeLight(self): 
        self.greenLight = "green"
        self.redLight = "darkred"
        self.yellowLight = "goldenrod4"
        self.__color = "Green"
        print("Feu vert") 
        
       


    def stopLight(self): 
        self.greenLight = "darkgreen"
        self.redLight = "red"
        self.yellowLight = "goldenrod4"
        self.__color = "Red"
        print("Feu rouge")


    def cautionLight(self): 
        self.greenLight = "darkgreen"
        self.redLight = "darkred"
        self.yellowLight = "yellow"
        self.__color = "Yellow"
        print("Feu jaune")
    #une nouvelle methode    
    def getColor(self):
         return self.__color
    
        ## Ici le jaune doit clignoter, 
        # mais pour l'instant on ne peut pas le faire en console, donc on va juste afficher un message
        