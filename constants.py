import numpy
import random


# define variables
Amplitude = numpy.pi/4
Frequency = 10
Offset = 0
frontLegAmplitude = 0.9
frontLegFrequency = 10.5
frontLegPhaseOffset = 0.0

# active variables
numberOfGenerations = 275

populationSize = 10

sleepDuringSimulation = "on"

sleepTime = 1/100

motorJointRange = 0.3

numOfRun = 5

seed = 5
#

numSensorNeurons = 1

numMotorNeurons = 1

rand_seed1 = random.randint(40, 100)
rand_seed2 = random.randint(40, 80)
rand_seed3 = random.randint(20, 120)
rand_seed4 = random.randint(10, 90)
rand_seed5 = random.randint(0, 35)
rand_seed6 = random.randint(40, 100) *2
rand_seed7 = random.randint(40, 80) /2 + 1
rand_seed8 = random.randint(20, 120) /2 +1
rand_seed9 = random.randint(10, 90) *2
rand_seed10 = random.randint(0, 35) *2










motorForce = 60