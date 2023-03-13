import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure 


with open('OverallFitness_init.txt', 'r') as file:
    data1 = []
    for line in file:
        row = [float(x) for x in line.split()]
        data1.append(row)

max_values1 = []
for sublist in data1:
    max_value1 = max(sublist)
    max_values1.append(max_value1)

del max_values1[100:375]


with open('OverallFitness_init2.txt', 'r') as file:
    data2 = []
    for line in file:
        row = [float(x) for x in line.split()]
        data2.append(row)

max_values2 = []
for sublist in data2:
    max_value2 = max(sublist)
    max_values2.append(max_value2)


with open('OverallFitness_init3.txt', 'r') as file:
    data3 = []
    for line in file:
        row = [float(x) for x in line.split()]
        data3.append(row)

max_values3 = []
for sublist in data3:
    max_value3 = max(sublist)
    max_values3.append(max_value3)
    
    
    
with open('OverallFitness_init_4.txt', 'r') as file:
    data4 = []
    for line in file:
        row = [float(x) for x in line.split()]
        data4.append(row)

max_values4 = []
for sublist in data4:
    max_value4 = max(sublist)
    max_values4.append(max_value4)



with open('OverallFitness_init5.txt', 'r') as file:
    data5 = []
    for line in file:
        row = [float(x) for x in line.split()]
        data5.append(row)

max_values5 = []
for sublist in data5:
    max_value5 = max(sublist)
    max_values5.append(max_value5)
    
    


with open('OverallFitness_init6.txt', 'r') as file:
    data6 = []
    for line in file:
        row = [float(x) for x in line.split()]
        data6.append(row)

max_values6 = []
for sublist in data6:
    max_value6 = max(sublist)
    max_values6.append(max_value6)



with open('OverallFitness_72.txt', 'r') as file:
    data7 = []
    for line in file:
        row = [float(x) for x in line.split()]
        data7.append(row)

max_values7 = []
for sublist in data7:
    max_value7 = max(sublist)
    max_values7.append(max_value7)



with open('OverallFitness_init8.txt', 'r') as file:
    data8 = []
    for line in file:
        row = [float(x) for x in line.split()]
        data8.append(row)

max_values8 = []
for sublist in data8:
    max_value8 = max(sublist)
    max_values8.append(max_value8)


with open('OverallFitness_fin9.txt', 'r') as file:
    data9 = []
    for line in file:
        row = [float(x) for x in line.split()]
        data9.append(row)

max_values9 = []
for sublist in data9:
    max_value9 = max(sublist)
    max_values9.append(max_value9)



with open('OverallFitness_10.txt', 'r') as file:
    data10 = []
    for line in file:
        row = [float(x) for x in line.split()]
        data10.append(row)

max_values10 = []
for sublist in data10:
    max_value10 = max(sublist)
    max_values10.append(max_value10)


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

ylabs = np.arange(0, 300, 75)
plt.xlabel('Number of Generations')
plt.ylabel('Best Fitness per Generation')
plt.title('Fitness curves over 300 generations')
#plt.yticks(ylabs)
ax = plt.gca()
ax.invert_yaxis()
plt.xticks(ylabs, ('0', '100', '200', '300'))
plt.show()



# from matplotlib import pyplot as plt
# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True
# line1, = plt.plot([1, 2, 3], label="line1")
# line2, = plt.plot([3, 2, 1], label="line2")

# plt.show()
