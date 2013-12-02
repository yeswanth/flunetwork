#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from Network import Network
from GraphStatistics import *

class DSNSimulation(object):

    def __init__(self):
        self.totalInfected = 0
        self.runtime = 150

    def initializeSimulation(self):
        self.network = Network()
        self.network.setInfected()
        self.network.setVaccinated()
        self.totalInfected = len(self.network.infectedNodes)

    def runSimulation(self):
        # for-while
        timeInstant = 0
        allstats = []
        json_outfile = open('stats.json', 'w')
        
        while timeInstant < self.runtime:
            graphStatistics = GraphStatistics()
            graphStatistics.resetStatistics()
            graphStatistics.timeInstant = (timeInstant + 1)
            self.network.runSimulationForTimeInstant(graphStatistics)
            graphStatistics.displayStatistics()
            self.totalInfected += graphStatistics.numberOfNewlyInfectedNodes
            timeInstant += 1
            allstats.append(graphStatistics)
        
        json.dump(allstats, json_outfile, default=GraphStatistics_encoder, indent=4)
        json_outfile.write("\n")
        json_outfile.close()
        
        print("\n\nWrote statistics to " + json_outfile.name + "\n\n")

    def endSimulation(self):
        print "------------------------- Ending Simulation -------------------------"
        print "Total number of nodes infected during simulation : " , self.totalInfected


if __name__ == '__main__':
    dsnSimulation = DSNSimulation()
    dsnSimulation.initializeSimulation()
    dsnSimulation.runSimulation()
    dsnSimulation.endSimulation()

