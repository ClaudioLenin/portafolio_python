# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 17:18:13 2023

@author: HP
"""

import numpy as np
import random

class DNA():
    def __init__(self,target,mutation_rate,n_individuals,n_selection,n_generations,verbose = True):
        self.target = target
        self.mutation_rate = mutation_rate
        self.n_individuals = n_individuals
        self.n_selection = n_selection
        self.n_generations = n_generations
        self.verbose = verbose
        
    def create_individual(self,min = 0,max = 9):        
        individual = [np.random.randint(min,max) for i in range(len(self.target))]
        return individual
        
    def create_population(self):
        population = [self.create_individual() for i in range(self.n_individuals)]
        return population
    
    def fitness(self,individual):
        #Evaluar el individuo
        fitness = 0
        
        for i in range(len(individual)):
            if individual[i] == self.target[i]:
                fitness += 1 
        return fitness
    
    def selection(self,population):
        scores = [(self.fitness(i),i) for i in population]
        scores = [i[1] for i in sorted(scores)]
        
        selected = scores[len(scores) - self.n_selection:]
        return selected
    
    def reproduction(self,population,selected):
        point = 0
        father = []
        
        for i in range(len(population)):
            point = np.random.randint(1,len(self.target)-1)
            father = random.sample(selected,2)
            
            population[i][:point] = father[0][:point]
            population[i][point:] = father[1][point:]
        return population
    
    def mutation(self,population):
        for i in range(len(population)):
            if random.random() <= self.mutation_rate:
                point = random.randint(1,len(self.target) - 1)
                new_value = np.random.randint(0,9)
                
                while new_value == population[i][point]:
                    new_value = np.random.randint(0,9)
                    
                population[i][point] = new_value
        return population
    
    def run_geneticapp(self):
        population = self.create_population()
        
        for i in range(self.n_generations):
            if self.verbose:
                print('_____________________')
                print('GENERACION: ',i)
                print('POBLACIÓN: ',population)
                
            selected = self.selection(population)
            population = self.reproduction(population,selected)
            population = self.mutation(population)
        
        
def main():
    target = [1,0,0,1,0,1,1]
    model = DNA(target = target,mutation_rate = 0.2,n_individuals = 15,n_selection = 5, n_generations = 50, verbose = True)
    model.run_geneticapp()

if __name__ == '__main__':
    main()
        