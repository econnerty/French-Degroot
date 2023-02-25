import numpy as np
import time
import matplotlib.pyplot as plt
import random as rand
n = 3

# Todo: Import agents from a csv with their trust scores
matrix = np.array([[1.0, .21,.43],[.47, .44,.33],[0.0,.21,.20]]) #Trust scores

agents = np.vstack(np.array([-.9, .65, -.124])) #Initial stance on opinion

tick = 1 #The first tick is considered the initial state
growth_rate = 1.000


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
    
    time.sleep(.5)
    