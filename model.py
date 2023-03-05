import numpy as np
import time
import matplotlib.pyplot as plt
import random as rand
import math


# Import realistic agents


agents = np.vstack(np.random.uniform(low=-1.0,high=1.0,size=250)) #Initial stance on opinion

matrix = np.random.rand(len(agents),len(agents)) #Trust scores

tick = 1 #The first tick is considered the initial state
growth_rate = 1.15 #The rate at which the agents resist opinion change

n = len(agents)


curr_agents = agents[0:].copy()

while(True):
    next_agents = curr_agents.copy()
    #Plot the data
    for i in range(n):
        plt.plot(agents[i])
    plt.show(block=False)
    plt.pause(0.0001)      
    for i in range(n):
        sum = 0
        for j in range(n):
            if(i == j):
                continue #The agent should not update its opinion on itself
            sum += (matrix[i,j]*((curr_agents[j]-curr_agents[i])))/growth_rate
        next_agents[i] = (curr_agents[i] + (sum/(n-1)))
    agents = np.append(agents,next_agents,axis=1)
    tick+=1
    curr_agents = np.vstack(agents[:,tick-1])
    
    growth_rate = growth_rate*growth_rate #idk why or how i decided this was right
    
    if (growth_rate >= math.inf):
        plt.ioff()
        plt.show()
        break
    