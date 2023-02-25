import numpy as np
import time
import matplotlib.pyplot as plt
n = 2

matrix = np.matrix('1 .5; .2 1') #Trust scores

agents = [np.array([.8,.1])] #Initial stance on opinion

tick = 1 #The first tick is considered the initial state


curr_agents = agents[0]

while(True):

    for i in range(n):
        for j in range(n):
            if(i == j):
                continue #The agent should not update its opinion on itself
            curr_agents[i] = ((matrix[i,j]*curr_agents[j])+((curr_agents[i]*tick)))/(tick+1) #This is not right
    agents.append(curr_agents)
    tick+=1
    
    #Plot the data
    plt.plot(agents)
    plt.show(block=False)
    
    while(True):
        userInput = input('Press Space')
        if (userInput == ' '):
            break
    