import pyrosim.pyrosim as pyrosim
import numpy as np
import os
import random
import time


class SOLUTION:
	def __init__(self, nextAvailableID):
		self.myID = nextAvailableID
		self.numMotorNeuron = 0
		self.numSensorNeuron = 0
		self.sensors = []
		self.motors = []
		self.neurons = 0
		self.links = []
		self.sizes = []
		self.linkposns = []
		self.mat = []
		self.colorvals = []
		self.joints = []
		self.jointposns = []
		self.jointaxes = []
		np.random.seed(random.randint(0,100))
		self.Init_Body()
		self.weights = np.random.rand(self.numSensorNeuron, self.numMotorNeuron) * 2 - 1
		
	def Start_Simulation(self, directOrGUI):
		if self.myID == 0:
			self.Create_World()
		self.Generate_Body()
		self.Generate_Brain()
		os.system("python simulate.py " + directOrGUI + " " + str(self.myID)+" &")

	def Wait_For_Simulation_To_End(self):
			fitFile = "fitness" + str(self.myID) + ".txt"
			while not os.path.exists(fitFile):
				time.sleep(1/100)
			fitnessFile = open(fitFile, "r")
			fit = fitnessFile.read()
			self.fitness = float(fit)
			fitnessFile.close()
			os.system("del " + fitFile)

	def Create_World(self):
		pyrosim.Start_SDF("world.sdf")
		pyrosim.End()

	def Generate_Body(self):
		pyrosim.Start_URDF("body"+str(self.myID)+".urdf")
		self.Build_Body()
		pyrosim.End()
  
	# def Init_Body(self): attempt to optimize and give up!
	# 	self.length = random.randint(4, 6)
	# 	for i in range(self.length):
	# 		self.Random_Color()
	# 		self.Random_Size()
	# 		self.links.append("TorsoLimb" + str(i))
	# 		self.linkposns.append(self.Random_Position() if i != self.length - 1 else self.linkposn)
	# 		self.mat.append(self.material)
	# 		self.colorvals.append(self.color)
	# 		self.sizes.append([self.X, self.Y, self.Z])
	# 		if i == 0:
	# 			self.axis = "x"
	# 			self.jointaxes.append(self.Random_Axis())
	# 			self.jointposns.append([self.X/2, 0, 1])
    # elif i < self.length - 1:
    #         self.jointaxes.append(self.Random_Axis())
    #         self.Random_Joint(i)
    #         self.joints.append("TorsoLimb" + str(i) + "_TorsoLimb" + str(i + 1))
    #         self.jointposns.append(self.jointPosition)
    # self.numSensorNeuron = self.mat.count("Green")
    # self.numMotorNeuron = len(self.joints)

	#got this idea from campuswire// suboptimal 
	def Init_Body(self):
		self.length = random.randint(4,6)
		for i in range(self.length+1):
			self.Random_Color()
			self.Random_Size()
			if i == 0:
				self.axis ="x"
				self.links.append("TorsoLimb" + str(i))
				self.linkposns.append([0,0,1])
				self.mat.append(self.mat)
				self.colorvals.append(self.color)
				self.sizes.append([self.X, self.Y, self.Z])
				self.jointaxes.append(self.Random_Axis())
				self.joints.append("TorsoLimb" + str(i) + "_TorsoLimb" + str(i + 1))
				self.jointposns.append([self.X/2,0,1])
			elif i==self.length:
				self.Random_Position()
				self.links.append("TorsoLimb" + str(i))
				self.linkposns.append(self.linkposn)
				self.mat.append(self.material)
				self.colorvals.append(self.color)
				self.sizes.append([self.X, self.Y, self.Z])
			else:
				self.Random_Position()
				self.links.append("TorsoLimb"+str(i))
				self.linkposns.append(self.linkposn)
				self.mat.append(self.material)
				self.colorvals.append(self.color)
				self.sizes.append([self.X,self.Y,self.Z])
				self.jointaxes.append(self.Random_Axis())
				self.joints.append("TorsoLimb"+str(i)+"_TorsoLimb"+str(i+1))
				self.Random_Joint(i)
				self.jointposns.append(self.jointPosition)
		self.numSensorNeuron = self.mat.count("Green")
		self.numMotorNeuron = len(self.joints)

	def Build_Body(self):
		for i in range(0,len(self.links)):
			pyrosim.Send_Cube(name=self.links[i], pos=self.linkposns[i], size=self.sizes[i],
									  materialName=self.mat[i],colorRgba=self.colorvals[i])
			if self.mat[i] == "Green":
				self.sensors.append(self.links[i])
		for i in range(0,len(self.joints)):
			pyrosim.Send_Joint(name=self.joints[i], parent=self.links[i], child=self.links[i+1], type="revolute",
								   position=self.jointposns[i], jointAxis=self.jointaxes[i])
			self.motors.append(self.joints[i])

	def Generate_Brain(self):
		pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
		for i in range(len(self.sensors)):
			pyrosim.Send_Sensor_Neuron(name=self.neurons, linkName=self.sensors[i])
			self.neurons +=1
		for i in range(len(self.motors)):
			pyrosim.Send_Motor_Neuron(name=self.neurons, jointName=self.motors[i])
			self.neurons +=1
		for currentRow in range(self.numSensorNeuron):
			for currentColumn in range(self.numMotorNeuron):
				pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+self.numSensorNeuron, weight=self.weights[currentRow][currentColumn])
		pyrosim.End()
		self.neurons = 0
		self.sensors.clear()
		self.motors.clear()

	def Mutate(self):
		self.linkindices = random.randint(1,len(self.links)-2)
		if self.mat[self.linkindices] == "Green":
			self.mat[self.linkindices] = "Blue"
			self.colorvals[self.linkindices] = "0 0 2.5 1.0"
		else:
			self.mat[self.linkindices] = "Green"
			self.colorvals[self.linkindices] = "0 1.2 0 1.0"
		if random.randint(0, 100) < 50:
			self.Random_Size()
			self.sizes[self.linkindices] = [self.X,self.Y,self.Z]
			self.Mutate_Positions()
		if random.randint(0, 100) < 50:
				self.Add_Limb()
		else:
				self.Remove_Limb()
		self.numSensorNeuron = self.mat.count("Green")
		self.numMotorNeuron = len(self.joints)
		self.weights = np.random.rand(self.numSensorNeuron, self.numMotorNeuron) * 2 - 1

	def Set_ID(self, ID):
		self.myID = ID
  
	def Random_Color(self):
		if random.randint(0, 100) < 50:
			self.material = "Green"
			self.color = "0 1.2 0 1.0"
		else:
			self.material = "Blue"
			self.color = "0 0 2.5 1.0"
   
	def Random_Size(self):
		self.X = random.uniform(0.2, .9)
		self.Y = random.uniform(0.2, .9)
		self.Z = random.uniform(0.2, .9)
  
	def Random_Joint(self, i):
		pos_choices = {
			'x': [[self.sizes[i][0] / 2, 0, self.sizes[i][2] / 2], [0, self.sizes[i][1] / 2, self.sizes[i][2] / 2]],
			'y': [[self.sizes[i][0] / 2, self.sizes[i][1] / 2, 0], [self.sizes[i][0] / 2, 0, self.sizes[i][2] / 2]],
			'z': [[0, self.sizes[i][1] / 2, self.sizes[i][2] / 2], [self.sizes[i][0] / 2, self.sizes[i][1] / 2, 0]]
		}
		if self.linkposns[i][0] != 0:
			self.jointPosition = random.choice(pos_choices['y' if self.linkposns[i][1] == 0 else 'z'])
			self.axis = "y" if self.jointPosition[1] != 0 else "z"
		elif self.linkposns[i][1] != 0:
			self.jointPosition = random.choice(pos_choices['x' if self.linkposns[i][0] == 0 else 'z'])
			self.axis = "x" if self.jointPosition[0] != 0 else "z"
		else:
			self.jointPosition = random.choice(pos_choices['x' if self.linkposns[i][0] == 0 else 'y'])
			self.axis = "x" if self.jointPosition[0] != 0 else "y"

	def Random_Position(self):
		if self.axis == "x":
			self.linkposn = [self.X/2,0,0]
		elif self.axis == "y":
			self.linkposn = [0,self.Y/2,0]
		else:
			self.linkposn = [0,0,self.Z/2]

	def Random_Axis(self):
		return random.choice(["1 0 0","0 1 0","0 0 1"])

	def Mutate_Positions(self):
			pos = [self.X / 2, self.Y / 2, self.Z / 2]
			if self.jointposns[self.linkindices][0] != 0:
				self.jointposns[self.linkindices][:3] = pos
			if self.linkposns[self.linkindices][0] != 0:
				self.linkposns[self.linkindices][:3] = pos
   
	def Add_Limb(self):
		self.Random_Color()
		self.Random_Size()
		nextLinkID = len(self.links)
		self.jointaxes.append(self.Random_Axis())
		self.joints.append("TorsoLimb" + str(nextLinkID-1) + "_TorsoLimb" + str(nextLinkID))
		self.Random_Joint(nextLinkID-2)
		self.jointposns.append(self.jointposns)
		self.Random_Position()
		self.links.append("TorsoLimb" + str(nextLinkID))
		self.linkposns.append(self.linkposn)
		self.mat.append(self.material)
		self.colorvals.append(self.color)
		self.sizes.append([self.X, self.Y, self.Z])

	def Remove_Limb(self):
		self.all_limbs = [self.links,self.sizes,self.linkposns,self.mat,self.colorvals
			,self.joints,self.jointposns,self.jointaxes]
		for body in self.all_limbs:
			body.pop()