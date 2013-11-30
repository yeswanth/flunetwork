#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Network import Network

class DSNSimulation(object):

    def __init__(self):
        self.totalInfected = 0
        self.runtime = 365

    def initializeSimulation(self):
        self.network = Network()
        self.network.setInfected()
        self.network.setVaccinated()
        self.totalInfected = self.network.getNumberOfInfectedNodes()

    def runSimulation(self):
        graphStatistics = GraphStatistics()
        ## for-while
        timeInstant = 0
        while timeInstant < self.runtime:
            graphStatistics.resetStatistics()
            graphStatistics.setTimeInstant(timeInstant)
            self.network.runSimulationForTimeInstant(graphStatistics)
            graphStatistics.displayStatistics()
            self.totalInfected += graphStatistics.getNumberOfNewlyInfectedNodes()
            timeInstant += 1

    def endSimulation(self):
        print "------------------------- Ending Simulation -------------------------"
        print "Total number of nodes infected during simulation : " + self.totalInfected


if __name__ == '__main__':
    dsnSimulation = DSNSimulation()
    dsnSimulation.initializeSimulation()
    dsnSimulation.runSimulation()
    dsnSimulation.endSimulation()
