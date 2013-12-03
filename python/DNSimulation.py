#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from Network import Network
from GraphStatistics import *

class DSNSimulation(object):

    def __init__(self):
        self.totalInfected = 0
        self.runtime = 150
	self.graphStatistics = []

    def initializeSimulation(self):
        self.network = Network()
        self.network.setInfected()
        self.network.setVaccinated()
        self.totalInfected = len(self.network.infectedNodes)

    def runSimulation(self):
        timeInstant = 0
        
        while timeInstant < self.runtime:
            self.graphStatistics[timeInstant].timeInstant = (timeInstant + 1)
            self.network.runSimulationForTimeInstant(self.graphStatistics[timeInstant])
            self.graphStatistics[timeInstant].displayStatistics()
            self.totalInfected += self.graphStatistics[timeInstant].numberOfNewlyInfectedNodes
            timeInstant += 1    

    def endSimulation(self):
        print "------------------------- Ending Simulation -------------------------"
        print "Total number of nodes infected during simulation : " , self.totalInfected


if __name__ == '__main__':
    count = 0
    dsnSimulation = DSNSimulation()
    while count < dsnSimulation.runtime:
	graphStatistic = GraphStatistics()
	graphStatistic.resetStatistics()
	dsnSimulation.graphStatistics.append(graphStatistic)
	count += 1

    count = 0
    while count < numberOfRunthroughs:
	dsnSimulation.initializeSimulation()
	dsnSimulation.runSimulation()
	dsnSimulation.endSimulation()
	count += 1

    json_outfile = open('stats.json', 'w')
    json.dump(dsnSimulation.graphStatistics, json_outfile, default=GraphStatistics_encoder, indent=4)
    json_outfile.write("\n")
    json_outfile.close()

    print("\n\nWrote statistics to " + json_outfile.name + "\n\n")
