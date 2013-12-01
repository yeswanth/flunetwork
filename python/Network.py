#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import copy
#import networkx as nx
#import matplotlib.pyplot as plt
from Node import Node


class Network(object):
        
    def __init__(self):
	#self.nxgraph = nx.Graph()
        self.graph = {} 
        self.numberOfNodes = 10000
        self.adjacentNodes = 15
        self.noInfected = 10
        self.noVaccinated = 1000
        self.globalDecayValue = 0.00000025
	self.proximityMultiplicationFactor = 5
        self.infectedNodes = set()
        self.varyingSusceptibilityNodes = set()
        self.loopListVariable = set()
        self._initializeGraph()

    def _initializeGraph(self):
        current_node = 0
        while current_node < self.numberOfNodes:
            self.graph[current_node] = Node()
	    #self.nxgraph.add_node(current_node)
            if (current_node != 0):
		count = 0
		while count < random.randrange(current_node):
		    neighbour = random.randrange(current_node)
		    if len(self.graph[current_node].neighbours) >= self.adjacentNodes:
		        break
		    if len(self.graph[neighbour].neighbours) >= self.adjacentNodes:
			count += 1
		        continue
		    self.graph[current_node].neighbours.add(neighbour)
		    self.graph[neighbour].neighbours.add(current_node)
		    print "Adding link between ", current_node, " and ", neighbour
		    #self.nxgraph.add_edge(current_node, neighbour)
		    count += 1
	    current_node += 1
	#nx.draw_random(self.nxgraph)
	#plt.show()

    def runSimulationForTimeInstant(self, graphStatistics):
        self.updateSusceptibilities()
	graphStatistics.nodesInfectedByDispersionEffect = self.proximityEffect()
        graphStatistics.numberOfRecoveredNodes = self.checkRecoveryState()
        graphStatistics.numberOfNewlyInfectedNodes = self.spreadInfection()
        graphStatistics.numberOfInfectedNodes = len(self.infectedNodes)

    def updateSusceptibilities(self):
        self.loopListVariable.clear()
        self.loopListVariable = copy.deepcopy(self.varyingSusceptibilityNodes)
        for currentNode in self.loopListVariable:
            if not self.graph[currentNode].updateSusceptibility():
                self.varyingSusceptibilityNodes.remove(currentNode)

    def checkRecoveryState(self):
        recoveredNodes = 0
        self.loopListVariable.clear()
        self.loopListVariable = copy.deepcopy(self.infectedNodes)
        for currentNode in self.loopListVariable:
            if self.graph[currentNode].isRecovered():
                print "+++Newly recovered node : " , currentNode
                recoveredNodes += 1
                self.infectedNodes.remove(currentNode)
                self.varyingSusceptibilityNodes.add(currentNode)
        return recoveredNodes

    def spreadInfection(self):
        newlyInfected = 0
        self.loopListVariable.clear()
        self.loopListVariable = copy.deepcopy(self.infectedNodes)
        for infectedNode in self.loopListVariable:
            for currentNode in self.graph.get(infectedNode).neighbours:
                if self.graph[currentNode].infect(self.globalDecayValue):
                    print "---Newly infected node : " , currentNode
                    newlyInfected += 1
                    self.infectedNodes.add(currentNode)
        return newlyInfected

    def proximityEffect(self):
	nodesInfectedByDispersionEffect = 0
	loopLimit = (len(self.infectedNodes) / float(self.numberOfNodes)) * self.proximityMultiplicationFactor
	count = 0
	while (loopLimit - count) > 0.5:
	    currentNode = random.randrange(self.numberOfNodes)
	    if self.graph[currentNode].forceInfect():
		self.infectedNodes.add(currentNode)
		print "Node infected by dispersion effect : " , currentNode
		nodesInfectedByDispersionEffect += 1
	    count += 1
	return nodesInfectedByDispersionEffect

    def setInfected(self):
        ## for-while
        count = 0
        while count < self.noInfected:
            infected_node = random.randrange(len(self.graph))
            if infected_node in self.infectedNodes:
                continue
            self.graph[infected_node].infected = True
            self.graph[infected_node].infectionTime = 0
            self.infectedNodes.add(infected_node)
            print "Added infected node : " , infected_node
            count += 1

    def setVaccinated(self):
        ## for-while
        count = 0
        while count < self.noVaccinated:
            vaccinated_node = random.randrange(len(self.graph))
	    if vaccinated_node in self.infectedNodes:
		continue
	    if vaccinated_node in self.varyingSusceptibilityNodes:
		count += 1
                continue
	    self.graph[vaccinated_node].vaccinate()
            self.varyingSusceptibilityNodes.add(vaccinated_node)
            print "Added vaccinated node : " , vaccinated_node
            count += 1
