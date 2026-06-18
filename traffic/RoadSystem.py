class RoadSystem:

    def __init__(self): 
        print("Initialisation du système routier")
        self.roadwidth = 100 
        self.canvaswidth = 800
        self.canvasheight = 800

    def drawRoads(self, canvas=None): 
        print("Affichage des routes")
        if canvas is not None:
            # Route Horizontale
            canvas.create_rectangle(
                0, 350, 800, 450,
                fill="gray", outline=""
            )
            # Route Verticale
            canvas.create_rectangle(
                350, 0, 450, 800,
                fill="gray", outline=""
            )
            # Marquages au sol
            self.drawRoadMarks(canvas)
    
    def drawRoadMarks(self, canvas=None):
        if canvas is not None:
            # Lignes pointillées verticales
            canvas.create_line(400, 0, 400, 350, fill="white", dash=(20, 20))
            canvas.create_line(400, 450, 400, 800, fill="white", dash=(20, 20))
            # Lignes pointillées horizontales
            canvas.create_line(0, 400, 350, 400, fill="white", dash=(20, 20))
            canvas.create_line(450, 400, 800, 400, fill="white", dash=(20, 20))