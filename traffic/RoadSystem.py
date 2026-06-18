class RoadSystem:

    def __init__(self): 
        print("Initialisation du système routier")
        #ajout des dimensions des routes
        self.roadwidth = 100 
        self.canvaswidth = 800
        self.canvasheight = 800
       
        self.drawRoads()

    def drawRoads(self,canvas=None): 
        print("Affichage des routes")
        #ajout de dessin des routes
        if canvas is not None:
            canvas.create_rectangle(
                0,
                350, 
                800,
                450,
                fill="gray")
            canvas.create_rectangle( 
                0,
                350,
                800,
                450,
                fill="gray"
            )
    
    def drawRoadMarks(self,canvas=None):
        
        canvas.create_line(
            400,
            0,
            400,
            350,
            fill="white",
            dash=(20,20)
        )
        
        canvas.create_line(
            400,
            450,
            400,
            800,
            fill="white",
            dash=(20,20)
        )