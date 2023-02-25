import numpy as np
import time
import matplotlib.pyplot as plt
import random as rand
n = 2

matrix = np.array([[1.0, 1.0],[.1, 1.0]]) #Trust scores

agents = np.vstack(np.array([1.0, -1.0])) #Initial stance on opinion

tick = 1 #The first tick is considered the initial state


curr_agents = agents[0:].copy()
while(True):
    next_agents = curr_agents.copy()
    print(next_agents)
    #Plot the data
    for i in range(n):
        plt.plot(agents[i])
    plt.show(block=False)
    for i in range(n):
        sum = 0
        for j in range(n):
            if(i == j):
                continue #The agent should not update its opinion on itself
            sum += matrix[i,j]*curr_agents[j]
        next_agents[i] = (curr_agents[i] + (sum/(tick)))
    agents = np.append(agents,next_agents,axis=1)
    tick+=1
    curr_agents = np.vstack(agents[:,tick-1])
    
    while(True):
        userInput = input()
        if (userInput == ' '):
            break
    