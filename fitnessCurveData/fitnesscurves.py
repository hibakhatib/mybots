import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure 

#I HATE MATPLOTLIB MOST DISORGANIZED DATA VIZ LIBRARY IN PYTHON

with open('fitness_1.txt', 'r') as file:
    data1 = [list(map(float, line.split())) for line in file]
max_values1 = [max(sublist) for sublist in data1]
del max_values1[100:375]

with open('fitness_2.txt', 'r') as file:
    data2 = [list(map(float, line.split())) for line in file]
max_values2 = [max(sublist) for sublist in data2]

with open('fitness_3.txt', 'r') as file:
    data3 = [list(map(float, line.split())) for line in file]
max_values3 = [max(sublist) for sublist in data3]

with open('fitness_4.txt', 'r') as file:
    data4 = [list(map(float, line.split())) for line in file]
max_values4 = [max(sublist) for sublist in data4]

with open('fitness_5.txt', 'r') as file:
    data5 = [list(map(float, line.split())) for line in file]
max_values5 = [max(sublist) for sublist in data5]

with open('fitness_6.txt', 'r') as file:
    data6 = [list(map(float, line.split())) for line in file]
max_values6 = [max(sublist) for sublist in data6]

with open('fitness_7_2.txt', 'r') as file:
    data7 = [list(map(float, line.split())) for line in file]
max_values7 = [max(sublist) for sublist in data7]

with open('fitness_8.txt', 'r') as file:
    data8 = [list(map(float, line.split())) for line in file]
max_values8 = [max(sublist) for sublist in data8]

with open('fitness_9_fin.txt', 'r') as file:
    data9 = [list(map(float, line.split())) for line in file]
max_values9= [max(sublist) for sublist in data9]

with open('fitness_10.txt', 'r') as file:
    data10 = [list(map(float, line.split())) for line in file]
max_values10 = [max(sublist) for sublist in data10]
        

#breakpoint()

line1, = plt.plot(range(1, len(max_values1[:-275]) + 1), (max_values1[:-275]), label = 'Seed 1')
line2, = plt.plot(range(1, len(max_values2) + 1), max_values2, label = 'Seed 2')
line3, = plt.plot(range(1, len(max_values3) + 1), max_values3, label = 'Seed 3')
line4, = plt.plot(range(1, len(max_values4) + 1), max_values4, label = 'Seed 4')
line5, = plt.plot(range(1, len(max_values5[:-17]) + 1), (max_values5[:-17]), label = 'Seed 5')
line6, = plt.plot(range(1, len(max_values6) + 1), max_values6, label = 'Seed 6')
line7, = plt.plot(range(1, len(max_values7[:-441]) + 1), (max_values7[:-441]), label = 'Seed 7')
line8, = plt.plot(range(1, len(max_values8[:-50]) + 1), (max_values8[:-50]), label = 'Seed 8')
line9, = plt.plot(range(1, len(max_values9[:-177]) + 1), (max_values9[:-177]), label = 'Seed 9')
line10, = plt.plot(range(1, len(max_values10[:-31]) + 1), (max_values10[:-31]), label = 'Seed 10')
leg = plt.legend(loc='lower right')

plt.xlabel('Number of Generations')
plt.ylabel('Best Fitness per Generation')
plt.title('Fitness curves over 300 generations')
ax = plt.gca()
ax.invert_yaxis()
plt.xticks(np.arange(0, 300, 75), ('0', '100', '200', '300'))
plt.show()