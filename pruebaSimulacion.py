import tkinter as tk
from GSimulacion import *

class Aplicacion:

    def __init__(self):
        self.ventana1=tk.Tk()

        NumeroParticulas = 3
        TiempoTotal = 20
        gsim =GSimulacion(NumeroParticulas,TiempoTotal,self.ventana1).start()
        #gsim.start_embedded()

        #self.fig = Figure()
        #self.graph = FigureCanvasTkAgg(self.fig, master=self.ventana1)
        #self.graph.get_tk_widget().pack(side="top",fill='both',expand=True) 
        self.ventana1.mainloop()

aplicacion1=Aplicacion()


#
