### CS396 Artifical Life Final Project 
Hiba Khatib 


### Brief notes on number of simulations
Project: Engineer Option


In my final project, I improved my A8 assignment and ran it for 300 generations on populations of 10 on 10 random seeds. 

Although the preferred task was 500 generations, the run time for my generations made this task unrealistic considering the time deadline. Each generation for a population of 10 was taking approximately 2-3 minutes. For 500 generations, 10 different times, this would have taken at least a week to run all generations (unless I understood incorrectly which is very possible). Minimizing the number of requested generations seemed to produce great results in comparison to my previous simulations while also running in a timely manner. 

### General Overview

Quick gif showing one evolution: 
<br>

insert gif here

<br>

Video showing evolution: 

Other fun bodies that emerged:

For my final project, I evolved random creatures in 3D. As opposed to my previous bodies, these creatures do not have a presupposed body shape and are randomized to a much greater degree. 

For every body, all joints contain motors and every pair of neurons contains synapses. There is a motor for every joint but sensors are added randomly with a 50/50 chance upon initial body creation. 

A blue colored link indicates that the link does not contain sensors while green indicates that link does contain a sensor. 

After cloning this repo, run the command "python search.py" in your terminal. You will see the initial body, then you will see values print to terminal before being asked to press enter to view evolved body. I recommend going into constants.py to change population size and generation size to view results quicker otherwise it will take several hours. 

### Body Genotype & Phenotype 

!['body](image.png)

Examples of randomly generated bodies:
(insert gif of bodies here)

### Brain Generation

!['brain'](image.png)


### Mutations & Parent/Child Genotypes



### Fitness & Fitness Curves



#### Citations 

Find pyrosim physics simulator here: 
Find more info about ludobots MOOC here: 

This project is for CS396 Artifical Life taught by Professor Sam Kriegman at Northwestern University. 

Deepest thanks to TA Donna Hooshmand for great support and mentorship throughout this class. 