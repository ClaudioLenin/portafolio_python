# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 20:57:53 2023

@author: HP
"""

import torch
import torch.nn as nn
import torch.optim as optim

#Predecir si un número es mayor o menor que 5
# Definir la arquitectura de la red neuronal
class SimpleNeuralNetwork(nn.Module):
    def __init__(self):
        super(SimpleNeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(1, 2)
        self.fc2 = nn.Linear(2, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Crear la red neuronal
simple_nn = SimpleNeuralNetwork()

# Definir la función de pérdida y el optimizador
criterion = nn.MSELoss()
optimizer = optim.SGD(simple_nn.parameters(), lr=0.01)

# Ejemplos de entrada y salida esperada
inputs = torch.tensor([[2.0], [4.0], [6.0], [8.0]])
expected_outputs = torch.tensor([[0.0], [0.0], [1.0], [1.0]])

# Entrenar la red neuronal
for epoch in range(1000):
    optimizer.zero_grad()
    outputs = simple_nn(inputs)
    loss = criterion(outputs, expected_outputs)
    loss.backward()
    optimizer.step()

# Guardar los parámetros de la red neuronal en un archivo
torch.save(simple_nn.state_dict(), 'parametros_red_neuronal.pth')

# Cargar los parámetros de la red neuronal desde el archivo
parametros = torch.load('parametros_red_neuronal.pth')
simple_nn.load_state_dict(parametros)

# Utilizar la red neuronal para hacer predicciones
inputs = torch.tensor([[1.0], [3.0], [5.0], [7.0], [9.0]])
predicted_outputs = simple_nn(inputs)
print(predicted_outputs)