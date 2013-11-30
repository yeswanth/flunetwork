#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Network(object):
    """ generated source for Network

    """
    random = Random()
    numberOfNodes = 100
    adjacentNodes = 10
    noInfected = 10
    noVaccinated = 10
    globalDecayValue = 0.00

    def getGraph(self):
        return graph

    def setGraph(self, graph):
        self.graph = graph

    def getVaryingSusceptibilityNodes(self):
        return varyingSusceptibilityNodes

    def setVaryingSusceptibilityNodes(self, varyingSusceptibilityNodes):
        self.varyingSusceptibilityNodes = varyingSusceptibilityNodes

    def getInfectedNodes(self):
        return infectedNodes

    def setInfectedNodes(self, infectedNodes):
        self.infectedNodes = infectedNodes

    def getLoopListVariable(self):
        return loopListVariable

    def setLoopListVariable(self, loopListVariable):
        self.loopListVariable = loopListVariable

    def __init__(self):
        self.random = Random()
        self.initializeGraph()

    def initializeGraph(self):
        ## for-while
        current_node = 0
        while current_node < self.numberOfNodes:
            graph.put(current_node, Node())
            if (current_node == 0):
                continue
            ## for-while
            count = 0
            while count < self.random.nextInt(current_node):
                neighbour = self.random.nextInt(current_node)
                if graph[current_node].getNeighbours().size() >= self.adjacentNodes:
                    break
                if graph[neighbour].getNeighbours().size() >= self.adjacentNodes:
                    continue
                graph[current_node].getNeighbours().add(neighbour)
                if graph[neighbour].getNeighbours().add(current_node):
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
        if not graph[currentNode].updateSusceptibility():
            varyingSusceptibilityNodes.remove(currentNode)

    def checkRecoveryState(self):
        recoveredNodes = 0
        loopListVariable.clear()
        loopListVariable.addAll(infectedNodes)
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


