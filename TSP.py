from sys import stdin
import math

params = list(map(int, stdin.readline().split()))
print(params)
numNodes = params[0]
nodeInfo = []
nodeSeries=[]
nodeSeries.append(1)
totalDistance = 0

first_edge_params = list(map(int, stdin.readline().split()))
originalx = first_edge_params[0]
originaly = first_edge_params[1]
currentnode = 1
currentx = originalx
currenty = originaly

##Construct the graph: using a list of tuples implementation
for i in range(params[0] - 1):
    node_params = list(map(int, stdin.readline().split()))
    node = (i + 2, node_params[0], node_params[1])
    nodeInfo.append(node)

numNodesCheck = len(nodeInfo)


q = 0
while q < numNodes - 1:
    lowestdistance = 0
    lowestnode = 0
    lowestx = 0
    lowesty = 0
    p = 0
    while p <= numNodesCheck - 1:
        testnode = nodeInfo[p][0]
        testx = nodeInfo[p][1]
        testy = nodeInfo[p][2]
        distance = math.sqrt((testx - currentx)*(testx - currentx)+
                         (testy - currenty)*(testy - currenty))
        if(lowestdistance == 0) or (distance < lowestdistance):
            lowestdistance = distance
            lowestnode = testnode
            lowestx = testx
            lowesty = testy
        p+=1
    totalDistance = totalDistance + lowestdistance
    nodeSeries.append(lowestnode)
    nodetoremove = (lowestnode,lowestx,lowesty)
    nodeInfo.remove(nodetoremove)
    currentnode = lowestnode
    currentx = lowestx
    currenty = lowesty
    numNodesCheck = numNodesCheck - 1
    q += 1
tripBack = math.sqrt((originalx - currentx)*(originalx - currentx)+
                         (originaly - currenty)*(originaly - currenty))
totalDistance = totalDistance + tripBack
print(totalDistance)
nodeSeries.append(1)
for i in range(len(nodeSeries)):
    print((nodeSeries[i]))