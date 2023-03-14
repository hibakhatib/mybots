### CS396 Artifical Life Final Project 
Hiba Khatib 


### Brief notes on number of simulations
Project: Engineer Option (44pts)


In my final project, I improved my A8 assignment and ran it for 300 generations on populations of 10 on 10 random seeds. 

Although the preferred task was 500 generations, the run time for my generations made this task unrealistic considering the time deadline. Each generation for a population of 10 was taking approximately 2-3 minutes. For 500 generations, 10 different times, this would have taken at least a week to run all generations (unless I understood incorrectly which is very possible). Minimizing the number of requested generations seemed to produce great results in comparison to my previous simulations while also running in a timely manner. 

### General Overview

Quick gif showing one evolution:  
<br>
![Evolutionary Robotics Teaser - Made with Clipchamp](https://user-images.githubusercontent.com/98929421/224638366-e6e78117-206e-42e9-b4c4-2a2197a687cd.gif)
<br>

Summary video: https://youtu.be/9DaIDKjyWWY

<br>

2 minute video showing numerous evolutions: https://youtu.be/QLFIh9ZBLcM

<br>

For my final project, I evolved random creatures in 3D. As opposed to my previous bodies, these creatures do not have a presupposed body shape and are randomized to a much greater degree. 

For every body, all joints contain motors and every pair of neurons contains synapses. There is a motor for every joint but sensors are added randomly with a 50/50 chance upon initial body creation. 

A blue colored link indicates that the link does not contain sensors while green indicates that link does contain a sensor. 

After cloning this repo, run the command "python search.py" in your terminal. You will see the initial body, then you will see values print to terminal before being asked to press enter to view evolved body. I recommend going into constants.py to change population size and generation size to view results quicker otherwise it will take several hours. 

### Body Genotype & Phenotype 

![image](https://user-images.githubusercontent.com/98929421/224853803-a0b8e540-5527-4b63-a8bb-88034648daf1.png)

### Brain Generation

![image](https://user-images.githubusercontent.com/98929421/224853845-ac0cc1ca-fe03-4950-99c3-0ed0168bd718.png)

### Mutations & Parent/Child Genotypes

The diagrams below explains the three different types of mutations. All of these mutations occurred at random. There was a mutation on every best robot per generation. The addition or removal of a link was a 50% chance while the synapse weights and sensor removals/link size changes occurred every time. 

<br>
    **This is the original body, prior to mutation** 
![image](https://user-images.githubusercontent.com/98929421/224854101-78e0b402-9d25-4631-ae8a-1e71c3da832a.png)
    
<br> 
    **The following illustrate possible changes to the original body resulting from each of the mutations** 
<br> 
    ![image](https://user-images.githubusercontent.com/98929421/224854243-ed4795d5-9d71-4cc5-b6e7-83794ed7cd47.png)
<br>
    ![image](https://user-images.githubusercontent.com/98929421/224854277-b7966a0b-5c3b-45fe-bad4-2dd9477a9804.png)
<br> 
    ![image](https://user-images.githubusercontent.com/98929421/224854314-ad3234f5-d0d6-4751-accc-93641a70a952.png)
<br>

### Fitness & Fitness Curves

The fitness is calculated as farthest absolute distance from the robot's starting point. At every generation, the robot that moved the farthest was selected as the best and set as the parent. The parent is then mutated and evolution is run where mutations occurred. Then the best robot is selected, and the process repeats until the end of the simulation. The final robot should have the highest fitness, meaning it achieved the farthest distance as a result of its mutations. 

![Final_fit_curve](https://user-images.githubusercontent.com/98929421/224611172-dd14414b-769f-42d4-b27b-07e8a2da5bae.png)

#### Citations 

Find pyrosim physics simulator here: https://github.com/jbongard/pyrosim
<br>
Find more info about ludobots MOOC here: https://www.reddit.com/r/ludobots/wiki/installation/
<br>

Karl Sims' paper which I referenced when building my diagrams: https://www.karlsims.com/papers/siggraph94.pdf 
<br>

This project is for CS396 Artifical Life taught by Professor Sam Kriegman at Northwestern University. 
<br>
Deepest thanks to TA Donna Hooshmand for great support and mentorship throughout. 
