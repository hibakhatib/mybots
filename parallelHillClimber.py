from solution import SOLUTION
import constants as c
import copy
import os
import numpy
import random

class PARALLEL_HILL_CLIMBER:

	def __init__(self):

		os.system("del brain.nndf")
		os.system("del Fitness.txt")
		os.system("del body.urdf")
		os.system("del OverallFitness.txt")

		self.parents ={}

		self.Best_Parent = None

		self.nextAvailableID = 0

		for i in range(c.populationSize):

			self.parents[i] = SOLUTION(self.nextAvailableID)

			self.nextAvailableID += 1

	def Evolve(self):

		self.parents[0].Start_Simulation("GUI")

		self.parents[0].Wait_For_Simulation_To_End()
		print("evaluating")

		self.Evaluate(self.parents)
  
		print("done evals")

		for currentGeneration in range(c.numberOfGenerations):
			print("now evolving")

			self.Evolve_For_One_Generation()
			print("done evolving for one gen")

	def Evolve_For_One_Generation(self):

		self.Spawn()

		self.Mutate()

		self.Evaluate(self.children)

		self.Print()

		self.Write_Overall_Fitness()

		self.Select()

	def Spawn(self):

		self.children = {}

		for parent in self.parents.keys():

			self.children[parent] = copy.deepcopy(self.parents[parent])

			self.children[parent].Set_ID(self.nextAvailableID)

			self.nextAvailableID += 1

	def Mutate(self):

		for child in self.children.keys():

			self.children[child].Mutate()

	def Select(self):

		for parent_key in self.parents.keys():

			if self.parents[parent_key].fitness > self.children[parent_key].fitness:
	
				self.parents[parent_key] = self.children[parent_key]

	def Print(self):

		for parent_key in self.parents.keys():

			print("")

			print("parent dist: ", self.parents[parent_key].fitness, "child dist: ", self.children[parent_key].fitness)

			print("")

	def Show_Best(self):

		Best_Parent_distance = -999

		for parent_key in self.parents.keys():

			if self.parents[parent_key].fitness > Best_Parent_distance:

				Best_Parent_distance = self.parents[parent_key].fitness

				self.Best_Parent = self.parents[parent_key]

		print("This is best distance:" + str(Best_Parent_distance))

		self.Best_Parent.Start_Simulation("GUI")

	def Evaluate(self, solutions):

		for i in range(c.populationSize):

			solutions[i].Start_Simulation("DIRECT")

		for i in range(c.populationSize):

			solutions[i].Wait_For_Simulation_To_End()

	def Write_Overall_Fitness(self):

		f = open("OverallFitness"+str(c.numOfRun)+".txt", 'a')

		for parent_key in self.parents.keys():

			f.write(str(self.parents[parent_key].fitness)+" ")

		f.write("\n")

		f.close()