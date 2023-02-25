import numpy as np
import time
import matplotlib.pyplot as plt
import random as rand
n = 2

matrix = np.matrix('1 .1 .2; .9 1 .3;1 1 1') #Trust scores

agents = [np.array([-1,1,.5])] #Initial stance on opinion

tick = 1 #The first tick is considered the initial state


curr_agents = agents[0]

while(True):

    #Plot the data
    plt.plot(agents)
    plt.show(block=False)
    for i in range(n):
        sum = 0
        for j in range(n):

            if(i == j):
                continue #The agent should not update its opinion on itself
            #if(rand.random() < matrix[i,j]):
            sum += matrix[i,j]*curr_agents[j] #This is not right
        print(sum/(n*tick))
        curr_agents[i] = curr_agents[i] + sum/(n*tick)
    agents.append(curr_agents)
    tick+=1
    
    while(True):
        userInput = input()
        if (userInput == ' '):
            break
    