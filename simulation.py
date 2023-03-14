import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time
from robot import ROBOT
from world import WORLD

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        self.solutionID = solutionID
        if self.directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI)
            p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        else:
            self.physicsClient = p.connect(p.DIRECT)    
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)
        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

    def Run(self):
        for i in range(1000):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            if self.directOrGUI == "GUI":
                time.sleep(1/100)

    def Get_Fitness(self, solutionID):
        self.robot.Get_Fitness(solutionID)
        
    def __del__(self):
        p.disconnect()
    