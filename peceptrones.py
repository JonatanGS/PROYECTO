# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:15:39 2020

@author: JohnnyGS
"""

#Importación de la librerías necesarias.
import numpy as np
import matplotlib.pyplot as plt

#Creación de la clase perceptrón.
class perceptron:
    
#Constructor con el número de entradas.
    def __init__(self, n):
        
        self.pesos=np.random.randn(n)
        self.n=n
    
#Propagación de los pesos para las entradas con la función step.
    def propagacion(self, entradas):
        
        self.salida=1*(self.pesos.dot(entradas)>0)
        self.entradas=entradas
        
#Actualización de pesos a valor medio.
    def actualizacion(self, lr, salidad):
        
        for i in range(0, self.n):
            self.pesos[i]=self.pesos[i]+lr*(salidad-self.salida)*self.entradas[i]
         
#Menú para seleccionar el tipo de perceptrón.
while True:
    tipo=int(input("Elija el perceptron que desea crear: "+'\n'+'\n'
          "1.- Preceptron AND."+'\n'
          "2.- Perceptron OR."+'\n'+'\n'
          "--> "))
    
    if tipo < 1 or tipo > 2:
        print("La opción elegida no es válida.")
        break
    
#Instanciación del perceptrón AND en memoria.
    if tipo == 1:
        perceptron_and=perceptron(4)

#Tabla puerta lógica AND.
        tabla=np.array([[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 1, 1]])

#Historial de pesos almacenados para representación.
        historial=[perceptron_and.pesos]
#Épocas a ejecutar.
        for epoca in range(0, 20):
            for i in range(0, 5):
                perceptron_and.propagacion(tabla[i,0:4])
                perceptron_and.actualizacion(0.5, tabla[i, 3])
#Concatenación de pesos totales en eje X.
                historial=np.concatenate((historial, [perceptron_and.pesos]), axis = 0)
                
#Representación gráfica.
        plt.plot(historial[:,0], 'c')
        plt.plot(historial[:,1], 'r')
        plt.plot(historial[:,2], 'b')
        plt.plot(historial[:,3], 'g')
        
        plt.show()
        break
    
    if tipo == 2:
        perceptron_or=perceptron(4)

        tabla=np.array([[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1]])

        historial=[perceptron_or.pesos]
        for epoca in range(0, 20):
            for i in range(0, 5):
                perceptron_or.propagacion(tabla[i,0:4])
                perceptron_or.actualizacion(0.5, tabla[i, 3])
                historial=np.concatenate((historial, [perceptron_or.pesos]), axis = 0)
                
        plt.plot(historial[:,0], 'c')
        plt.plot(historial[:,1], 'r')
        plt.plot(historial[:,2], 'b')
        plt.plot(historial[:,3], 'g')
        
        plt.show()
        break