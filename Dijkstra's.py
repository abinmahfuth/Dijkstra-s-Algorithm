'''
This code takes input of the distance matrix and outputs the shortest path to every other node in the graph.

Note that the distance matrix has to be symmetrical, i.e. the links are undirectional, and no node is connected to itself.

Written by Abdul Binmahfuth and completed on the 26th September, 2019

'''
import numpy as np

#A is the distance matrix
A = [[0,6,0,0,0,0,49,0,0,0,0,0,0],[6,0,0,0,6,0,48,0,0,0,0,0,0],[0,0,0,0,0,18,24,0,0,1,7,0,0],[0,0,0,0,17,28,0,19,30,0,0,0,0],[0,6,0,17,0,0,0,0,0,0,0,0,0],[0,0,40,22,0,0,19,4,0,0,0,0,0],[49,48,24,0,0,19,0,0,0,0,0,0,0],[0,0,0,20,0,4,0,0,0,0,0,0,0],[0,0,0,30,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,6,5,0],[0,0,6,0,0,0,0,0,0,7,0,7,8],[0,0,0,0,0,0,0,0,0,7,9,0,5],[0,0,0,0,0,0,0,0,0,0,8,4,0]] 
D = 0 #initialise the distance from the starting node
size = len(A)
Dist = np.zeros((size,size),int)
u = []
s = 0  #By default, the starting position is 0 (i.e. the first node)
k = s #initialise
p = k #visited nodes index
e = range(size)
j = 0

#Check the shortest path for all nodes
for c in e:
    D = 0
    k = j
    O=[]
    #Shortest path loop calculation for node c
    for x in e:
        r = 0
        y = k
      #Extract the starting node row
        S = A[k]
        S_temp = S
      #Adding to visited nodes list
        O.append(k)
        O_Ran = range(len(O))
        for h in O_Ran: #updating visited nodes
            t = O[h]
            S_temp[t] = 0
        #Make sure that we don't get a list of zero elements
        if sum(S_temp) == 0:
            for l in e:
                if l not in O:
                    u.append(l) #Store unvisited nodes in list U
            for m in range(len(u)):
                S_temp = A[u[m]]
                for h in O_Ran: #updating visited nodes
                     t = O[h] 
                     S_temp[t] = 0
                if sum(S_temp) != 0: #Check if unvisited node does not contain zero elements
                    u=[]
                    break
        if sum(S_temp) == 0:
            u=[]
            break
        #Find minimum value
        mini = min(i for i in S_temp if i > 0)
        #indexing the minimum value
        k = S_temp.index(mini)
        #Copy the values into the distance list
        for z in range(len(S_temp)):
            v_temp = Dist[c,y] + S_temp[z]
            if S_temp[z] > 0: #To make sure unvisited nodes don't get updated
               if Dist[c,z] > v_temp or Dist[c,z] == 0:
                  Dist[c,z] = v_temp
        D += mini
    k = 0
    j += 1    
# Mirror values along the diagonal
for i in e:
    for j in e:
        Dist[j,i] = Dist[i,j]

print("The distance list is: ")
print(Dist)

    
