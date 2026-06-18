from traffic.TrafficLight import TrafficLight

class TrafficLightSystem:

    def __init__(self, mbFeu: TrafficLight, mtFeu: TrafficLight, llFeu: TrafficLight, lrFeu: TrafficLight):
        print("Initialisation du système de feux de circulation")
        self.mbFeu = mbFeu
        self.mtFeu = mtFeu
        self.llFeu = llFeu
        self.lrFeu = lrFeu
        
        self.initializeTrafficLights()
        self.launchTrafficLightSystem()
        # Supprimé : self.drawTrafficLights() car l'interface GUI s'en occupe en lui passant le canvas
        self.currentState = "MAIN_GREEN"
        
    def switchState(self):
        if self.currentState == "MAIN_GREEN":
            self.cautionMainTraffic()
            self.currentState = "MAIN_YELLOW"
        elif self.currentState == "MAIN_YELLOW":
            self.authorizeLateralTraffic()
            self.currentState = "LATERAL_GREEN"
        elif self.currentState == "LATERAL_GREEN":
            self.cautionLateralTraffic()
            self.currentState = "LATERAL_YELLOW"
        else:
            self.authorizeMainTraffic()
            self.currentState = "MAIN_GREEN"
    
    def drawTrafficLights(self, canvas=None):
        print("Affichage des feux de circulation")
        if canvas is not None:
            self.mbFeu.drawLight(canvas)
            self.mtFeu.drawLight(canvas)
            self.llFeu.drawLight(canvas)
            self.lrFeu.drawLight(canvas)

    def initializeTrafficLights(self):
        print("Initialisation des feux de circulation")
        self.mbFeu.authorizeLight()
        self.mtFeu.authorizeLight()
        self.llFeu.stopLight()
        self.lrFeu.stopLight()

    def authorizeLateralTraffic(self):
        print("Autorisation du trafic latéral")
        self.mbFeu.stopLight()
        self.mtFeu.stopLight()
        self.llFeu.authorizeLight()
        self.lrFeu.authorizeLight()
    
    def authorizeMainTraffic(self):
        print("Autorisation du trafic principal")
        self.mbFeu.authorizeLight()
        self.mtFeu.authorizeLight()
        self.llFeu.stopLight()
        self.lrFeu.stopLight()
    
    def cautionMainTraffic(self):
        print("Mise en garde du trafic principal")
        self.mbFeu.cautionLight()
        self.mtFeu.cautionLight()
        self.llFeu.stopLight()
        self.lrFeu.stopLight()
    
    def cautionLateralTraffic(self):
        print("Mise en garde du trafic latéral")
        self.mbFeu.stopLight()
        self.mtFeu.stopLight()
        self.llFeu.cautionLight()
        self.lrFeu.cautionLight()

    def launchTrafficLightSystem(self):
        print("Lancement du système de feux de circulation")
        self.authorizeMainTraffic()