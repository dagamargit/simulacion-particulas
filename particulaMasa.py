from particula import *
class ParticulaMasa(Particula):
    def __init__(self):
        super().__init__()
        self.masa = 0

    def setValores(self, pPos, pVel, pAcc, pMasa):
        """
          Inicializa la posición y la velocidad con los valores dados
        """
        super().setValores(pPos, pVel, pAcc)
        self.masa = pMasa

    def initRandom(self):
        """
          Inicializa la posición y la velocidad de forma aleatoria
        """
        self.setValores(np.array([random(), random(), random() ]), np.array([random(), random(), random()]),
          np.array( [random(), random(), random()]), random())

    def muestra(self):
        """
          Muestra por Terminal los valores de los atributos
        """  
        super().muestra()
        #print("   La masa es: ", self.masa)

    def aceleracionCero(self):
        """ 
          Pone a cero la aceleración para el paso de tiempo siguiente
        """
        self.acc=np.array([0.0,0.0,0.0])
    
    def aceleracionGravitatoria(self, otra):
        """
           Calcula la aceleración provocada por la masa de la otra particula 
        """
        softening = 1e-6
           # prevents explosion in the case the particles are really close to each other 
        distancia = self.distancia (otra)
        if distancia < softening:
            distancia = softening
        distanciaInv = 1.0 / distancia
        delta = otra.pos - self.pos
        self.acc += delta* G * otra.masa * distanciaInv ** 3