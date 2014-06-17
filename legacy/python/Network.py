#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import copy
from Node import Node


class Network(object):
        
    def __init__(self):
        self.graph = {} 
        self.numberOfNodes = 100
        self.adjacentNodes = 10
        self.noInfected = 10
        self.noVaccinated = 10
        self.globalDecayValue = 0.00
        self.infectedNodes = set()
        self.varyingSusceptibilityNodes = set()
        self.loopListVariable = set()
        self._initializeGraph()


    def _initializeGraph(self):
        ## for-while
        current_node = 0
        while current_node < self.numberOfNodes:
            self.graph[current_node] = Node()
            if (current_node == 0):
                current_node += 1
                continue
            ## for-while
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
                print("Adding link between ", current_node, " and ", neighbour)
                count += 1
            current_node += 1

    def runSimulationForTimeInstant(self, graphStatistics):
        self.updateSusceptibilities()
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
                print("+++Newly recovered node : " , currentNode)
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
                    print("---Newly infected node : " , currentNode)
                    newlyInfected += 1
                    self.infectedNodes.add(currentNode)
        return newlyInfected

    def setInfected(self):
        ## for-while
        count = 0
        while count < self.noInfected:
            infected_node = random.randrange(len(self.graph))
            self.graph[infected_node].infected = True
            if infected_node in self.infectedNodes:
                continue

            self.infectedNodes.add(infected_node)
            self.graph[infected_node].infectionTime = 0
            print("Added infected node : " , infected_node)
            count += 1

    def setVaccinated(self):
        ## for-while
        count = 0
        while count < self.noVaccinated:
            vaccinated_node = random.randrange(len(self.graph))
            self.graph[vaccinated_node].vaccinate()
            if vaccinated_node in self.varyingSusceptibilityNodes:
                continue
            self.varyingSusceptibilityNodes.add(vaccinated_node)
            self.graph[vaccinated_node].infected = False
            try:
                self.infectedNodes.remove(vaccinated_node)
            except KeyError as e:
                print(e)
            print("Added vaccinated node : " , vaccinated_node)
            count += 1


