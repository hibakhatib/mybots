## CS396 Artifical Life Final Project 
Hiba Khatib 


## Brief notes on number of simulations
Project: Engineer Option (44pts)

In my final project, I improved my A8 assignment and ran it for 300 generations on populations of 10 on 10 random seeds. 

Although the preferred task was 500 generations, the run time for my generations made this task unrealistic considering the time deadline. Each generation for a population of 10 was taking approximately 2-3 minutes. For 500 generations, 10 different times, this would have taken at least a week to run all generations (unless I understood incorrectly which is very possible). Minimizing the number of requested generations seemed to produce great results in comparison to my previous simulations while also running in a timely manner. 

## Videos & Teaser

Quick gif showing one evolution:  
<br>
![Evolutionary Robotics Teaser - Made with Clipchamp](https://user-images.githubusercontent.com/98929421/224638366-e6e78117-206e-42e9-b4c4-2a2197a687cd.gif)
<br>

2 minute summary video: https://youtu.be/9DaIDKjyWWY

<br>

2 minute video showing numerous evolved body, before and after: https://youtu.be/QLFIh9ZBLcM

<br>

## General Overview

For my final project, I evolved random creatures in 3D. As opposed to my previous bodies, these creatures do not have a presupposed body shape and are randomized to a much greater degree. 

For every body, all joints contain motors and every pair of neurons contains synapses. There is a motor for every joint but sensors are added randomly with a 50/50 chance upon initial body creation. 

A blue colored link indicates that the link does not contain sensors while green indicates that link does contain a sensor. 

## Body Genotype & Phenotype 

The bodies are completely randomly generated. The simple recusion employed, as described in the figure below, only enforces the creation of another limb which branches on the previous limb. The main segment grows a segment randomly on its body, which grows another random segment, so on and so forth. The segments do not overlap and form a jumbled mess. The positions and sizes of every segment are stored in a list which is used to generate new segments appropriately on the body. 
![image](https://user-images.githubusercontent.com/98929421/224853803-a0b8e540-5527-4b63-a8bb-88034648daf1.png)

## Brain Generation

Prior to brain generation, the robots are able to sense and act but their sensors do not inform their actions. By generating the brain, we connect the robot's "sensor to its motors using a neural network comprised of neurons and synapses" (https://www.reddit.com/r/ludobots/wiki/neurons/). The inclusion of neurons and synapses allows for closed loop control of the robot in which the motor neurons send the angles to motors, which are then converted to torques and applied to joints, changing the robots steps and robot's sensors, and finally the synapses taking the values from the sensors back to the motors neurons. 

The brains are regenerated with every new body to accomdate changes within the body. 
![image](https://user-images.githubusercontent.com/98929421/224853845-ac0cc1ca-fe03-4950-99c3-0ed0168bd718.png)

## Mutations & Parent/Child Genotypes

The diagrams below explains the three different types of mutations. All of these mutations occurred at random. There was a mutation on every best robot per generation. The addition or removal of a link was a 50% chance while the synapse weights and sensor removals/link size changes occurred every time. 

<br>
    This is the original body, prior to mutation:
  
<img width="501" alt="image" src="https://user-images.githubusercontent.com/98929421/224864854-5c058f8d-11ad-4b79-a1a9-48336c7ff35a.png">
    
<br> 
    The following illustrate possible changes to the original body resulting from each of the mutations:
<br> 
<img width="475" alt="image" src="https://user-images.githubusercontent.com/98929421/224864949-2586b79a-eb2a-4dcb-a799-8b90c9f7f11c.png">
<br>
<img width="477" alt="image" src="https://user-images.githubusercontent.com/98929421/224865002-40bfe33f-ac75-4679-a532-54d5a61e01db.png">
<br> 
<img width="539" alt="image" src="https://user-images.githubusercontent.com/98929421/224865047-0485415e-cdde-4b03-a32e-158bbeca2d72.png">
*brief note about this diagram: the link does not exclusively have to be a motor neuron link, this is how I happened to draw the diagram which I now realize may be a little bit confusing. The link being removed/added is any link, including sensor neuron links*
<br>

## Selection & Fitness Curves

The fitness is calculated as farthest distance from the robot's starting point. In the figure, the better fitness is at values less than 0 because I wanted the robot to move away from our POV, in the negative direction. 
<br>
<br>
At every generation, the robot that moved the farthest was selected as the best and set as the parent. The parent is then mutated and evolution is run where mutations occurred. Then the best robot is selected, and the process repeats until the end of the simulation. The final robot should have the highest fitness, meaning it achieved the farthest distance as a result of its evolution. 

There are some points in the graph where there is a significant drop in fitness. This could be due to a bad mutation such as a body already having lost most of limbs, losing another important link and losing good mobility. 

![Final_fit_curve](https://user-images.githubusercontent.com/98929421/224611172-dd14414b-769f-42d4-b27b-07e8a2da5bae.png)

## Results & Observations 

From my 30,000 simulations, I was able to conclude the following: 

- smaller bodies are preferred as almost every robot, 7/10 of the random seeds, became smaller in size by the end of their evolution. 
- complexity leads to less fitness. The bodies that had more complex seeming bodies struggled to move around and often got stuck in place. Below is an example of a complex body which failed vs a simple body which performed well: 
![complexitygif](https://user-images.githubusercontent.com/98929421/225050536-6d087cdf-47c7-4264-b450-d1c83e46a671.gif)
- if the body was very complex but longer in the vertical direction, it performed better than less complex and much smaller bodies because it had more limbs touching the ground to attempt to use and move with. This often led to jumping and hopping. 

<br>
<br>
Some of these trends can be seen in this video: https://youtu.be/QLFIh9ZBLcM


## Running this locally

After cloning this repo, run the command "python search.py" in your terminal. You will see the initial body, then you will see values print to terminal before being asked to press enter to view evolved body. I recommend going into constants.py to change population size and generation size to view results quicker otherwise it will take several hours. 

### Citations 

Find pyrosim physics simulator here: https://github.com/jbongard/pyrosim
<br>
Find more info about ludobots MOOC here: https://www.reddit.com/r/ludobots/wiki/installation/
<br>
Karl Sims' paper which I referenced when building my diagrams: https://www.karlsims.com/papers/siggraph94.pdf 
<br>

This project is for CS396 Artifical Life taught by Professor Sam Kriegman, professor and creator of xenobots, at Northwestern University. Check out his work here: https://www.xenobot.group/.
<br>

*Deepest* thanks to TA Donna Hooshmand for great support and mentorship throughout. 
