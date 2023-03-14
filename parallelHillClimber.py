from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:

	def __init__(self):
		os.system("del brain.nndf")
		os.system("del Fitness.txt")
		os.system("del body.urdf")
		os.system("del OverallFitness.txt")
  
		self.nextAvailableID = 0
		self.parents = {}
		self.Best = None
		for i in range(c.population):
			self.parents[i] = SOLUTION(self.nextAvailableID)
			self.nextAvailableID += 1

	def Evolve(self):
     #this seems to working same way 
		self.parents[0].Start_Simulation("GUI")
		self.parents[0].Wait_For_Simulation_To_End()
		#print("evaluating")
		self.Evaluate(self.parents)
		#print("done evals")
		for currentGeneration in range(c.generations):
			#print("now evolving")
			self.Evolve_For_One_Generation()
			#print("done evolving for one gen")

	def Evolve_For_One_Generation(self):
		self.Spawn()
		self.Mutate()
		self.Evaluate(self.children)
		self.Print()
		self.Save_Fitness()
		self.Select()
  
	def Evaluate(self, solutions):
			for sol in range(c.population):
				solutions[sol].Start_Simulation("DIRECT")
			for sol in range(c.population):
				solutions[sol].Wait_For_Simulation_To_End()
    
	def Spawn(self):
		self.children = {}
		for parent in self.parents.keys():
			self.children[parent] = copy.deepcopy(self.parents[parent])
			self.children[parent].Set_ID(self.nextAvailableID)
			self.nextAvailableID += 1

	def Mutate(self):
		for i in self.children.keys():
			self.children[i].Mutate()
   
	def Print(self):
		for parent in self.parents.keys():
			print("parent fitness: " + str(self.parents[parent].fitness) + "\n")
			print("child fitness: " + str(self.children[parent].fitness) + "\n")

	def Select(self):
		for parent in self.parents.keys():
			if self.parents[parent].fitness > self.children[parent].fitness:
				self.parents[parent] = self.children[parent]

	def Show_Best(self):
     #moved gui line for first up
		highest_fitness = 0
		for parent in self.parents.keys():
			if self.parents[parent].fitness < highest_fitness:
				highest_fitness = self.parents[parent].fitness
				self.Best = self.parents[parent]
		print("best fitness: " + str(highest_fitness) + "\n")
		self.Best.Start_Simulation("GUI")

	def Save_Fitness(self):
		f = open("fitness.txt", 'a')
		for parent in self.parents.keys():
			f.write(str(self.parents[parent].fitness)+" \n")
		f.close()