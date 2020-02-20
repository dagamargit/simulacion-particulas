from particulaMasa import *
from random import random, seed
from math import sqrt
import matplotlib.pyplot as plt
import time
from mpl_toolkits import mplot3d
pausa = 0.02

class GSimulacion:
        
    def __init__(self, NumParticulas, tiempoTot):
        self.N = NumParticulas
        self.tiempoTot = tiempoTot
        self.particulas = []
        for _ in range(0,self.N):
            self.particulas.append(ParticulaMasa())
        self.initPos()  
        self.initVel() 
        self.initMasa()
        self.deltat = 0.1
        self.tiempo =0.0
        self.preparaGrafico()
        self.refrescaParticulas() 

    def initPos(self):
        """
            Iniciliza las 3 primeras posiciones a valores fijos y el resto aleatorios
        """
        
        self.particulas[0].pos=np.array([0.,0.,0.])
        self.particulas[1].pos=np.array([1,1,0.])
        self.particulas[2].pos=np.array([1.2,0.25,0.])
        seed()
        for i in range(3,self.N):
            self.particulas[i].pos =np.array([random()*2-1,random()*2-1,random()*2-1])

    def initVel(self):
        """
            Iniciliza las 3 primeras velocidades a valores fijos y el resto aleatorios
        """

        self.particulas[0].vel=np.array([0.,0.,0.])
        self.particulas[1].vel=np.array([0,0.5,0.])
        self.particulas[2].vel=np.array([0,0.5,0.])
        seed()
        for i in range(3,self.N):
            # self.particulas[i].vel =[random()*2-1,random()*2-1,random()*2-1]
            self.particulas[i].vel =np.array([0.,0.5,0.])

    def initMasa(self):
        """
            Iniciliza la primera masa a 1.0e10 (grande) y el resto a 1.0e5 
        """
        self.particulas[0].masa = 1.0e10
        for i in range(1,self.N):
            self.particulas[i].masa = 1.0e5

    def preparaGrafico(self):
        plt.ion()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111,projection='3d')

        self.ax.set_xlim(-2.5,2.5)
        self.ax.set_ylim(-2.5,2.5)
        self.ax.set_zlim(-2.5,2.5)

        self.grafico = self.ax.scatter([],[],[],c='r',marker='o')
        plt.draw()


    def refrescaParticulas(self):
       
        self.grafico.remove() #Limpia el gráfico para mostrar las posiciones nuevas
        col=['g']   # La primera verde y el resto rojas
        for _ in range (1,self.N):
            col.append('r')
        x,y,z = self.vectoriza()    
        # plt.title("Partículas. Tiempo= "+ str(self.tiempo))
        self.grafico = self.ax.scatter(x,y,z,c=col,marker='o')
        # self.ax.view_init(30, 30)
        plt.draw()
        plt.pause(pausa)

    def printParticulas(self):
        for i in range(0,self.N):
            self.particulas[i].muestra()

    def cabecera(self):
        print ("Inicio de la simulación")

    def vectoriza(self):
        x=[]
        y=[]
        z=[]
        for i in range(0,self.N):
            x.append(self.particulas[i].pos[0])
            y.append(self.particulas[i].pos[1])
            z.append(self.particulas[i].pos[2])

        return x,y,z

    def pasoSimulacion(self):
        for i in range (0,self.N):# update acceleration
            self.particulas[i].aceleracionCero()
            for j in range (0, self.N):
                    if (i!=j):
                        self.particulas[i].aceleracionGravitatoria(self.particulas[j])
        
        for i in range (0,self.N):#update vel and pos
                self.particulas[i].actualizaVelocidadYPosicion(self.deltat)        

    def start(self):
        self.cabecera()
        
        while self.tiempo <= self.tiempoTot: 
            # print ("Timepo:", self.tiempo)
            self.printParticulas()
            self.pasoSimulacion()
            self.refrescaParticulas()
            self.tiempo += self.deltat
 
        print ("Fin particulas")
        # plt.plot()
        # plt.close('all')


