#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from Node import Node


class Network(object):
        
    def __init__(self):
        self.graph = {} 
        self.numberOfNodes = 100
        self.adjacentNodes = 10
        self.noInfected = 10
        self.noVaccinated = 10
        self.globalDecayValue = 0.00
        self._initializeGraph()


    def _initializeGraph(self):
        ## for-while
        current_node = 0
        while current_node < self.numberOfNodes:
            print current_node
            self.graph[current_node] = Node()
            if (current_node == 0):
                continue
            ## for-while
            count = 0
            while count < random.randrange(current_node):
                print "Count= ", count
                neighbour = random.randrange(current_node)
                if self.graph[current_node].neighbours.size() >= self.adjacentNodes:
                    break
                if self.graph[neighbour].neighbours.size() >= self.adjacentNodes:
                    continue
                self.graph[current_node].neighbours.add(neighbour)
                if self.graph[neighbour].neighbours.add(current_node):
                    print "Adding link between " + current_node + " and " + neighbour
                count += 1
            current_node += 1

    def runSimulationForTimeInstant(self, graphStatistics):
        self.updateSusceptibilities()
        graphStatistics.setNumberOfRecoveredNodes(self.checkRecoveryState())
        graphStatistics.setNumberOfNewlyInfectedNodes(self.spreadInfection())
        graphStatistics.setNumberOfInfectedNodes(len(infectedNodes))

    def getNumberOfInfectedNodes(self):
        return len(infectedNodes)

    def updateSusceptibilities(self):
        loopListVariable.clear()
        loopListVariable.addAll(varyingSusceptibilityNodes)
        for currentNode in lostListVariable:
            if not graph[currentNode].updateSusceptibility():
                varyingSusceptibilityNodes.remove(currentNode)

    def checkRecoveryState(self):
        recoveredNodes = 0
        loopListVariable.clear()
        loopListVariable.addAll(infectedNodes)
        for currentNode in loopListVariable:
            if graph[currentNode].isRecovered():
                print "+++Newly recovered node : " + currentNode
                recoveredNodes += 1
                infectedNodes.remove(currentNode)
                varyingSusceptibilityNodes.add(currentNode)
        return recoveredNodes

    def spreadInfection(self):
        newlyInfected = 0
        loopListVariable.clear()
        loopListVariable.addAll(infectedNodes)
        for currentNode in loopListVariable:
            for currentNode in graph.get(infectedNode).neighbours():
                if graph[currentNode].infect(self.globalDecayValue):
                    print "---Newly infected node : " + currentNode
                    newlyInfected += 1
                    infectedNodes.add(currentNode)
        return newlyInfected

    def setInfected(self):
        ## for-while
        count = 0
        while count < self.noInfected:
            infected_node = self.random.nextInt(len(graph))
            graph[infected_node].setInfected(True)
            if not infectedNodes.add(infected_node):
                count -= 1
                continue
            graph[infected_node].setInfectionTime(0)
            print "Added infected node : " + infected_node
            count += 1

    def setVaccinated(self):
        ## for-while
        count = 0
        while count < self.noVaccinated:
            vaccinated_node = self.random.nextInt(len(graph))
            graph[vaccinated_node].vaccinate()
            if not varyingSusceptibilityNodes.add(vaccinated_node):
                count -= 1
                continue
            graph[vaccinated_node].setInfected(False)
            infectedNodes.remove(vaccinated_node)
            print "Added vaccinated node : " + vaccinated_node
            count += 1


