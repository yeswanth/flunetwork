#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import copy

from Network import Network
from GraphStatistics import *

class DSNSimulation(object):

    def __init__(self):
        self.totalInfected = 0
        self.runtime = 150
	self.graphStatistics = []

    def initializeSimulation(self, recoveryRate):
        self.network = Network(recoveryRate)

    def initializeSimulation2(self, percentVaccinated):
        self.network.setInfected()
	self.network.noVaccinated = percentVaccinated
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
    #total = []
    #loop = 0.002
    #while loop <= 0.1:
    """
    count = 0
    dsnSimulation = DSNSimulation()
    while count < dsnSimulation.runtime:
	graphStatistic = GraphStatistics()
	graphStatistic.resetStatistics()
	dsnSimulation.graphStatistics.append(graphStatistic)
	count += 1
    count = 0
    while count < numberOfRunthroughs:
	dsnSimulation.initializeSimulation(0.1, 0.002167)
	dsnSimulation.runSimulation()
	dsnSimulation.endSimulation()
	count += 1
    """

    statistics = []
    vaccinationValues = []
    vaccinationValues.append(0.0)
    vaccinationValues.append(0.1)
    vaccinationValues.append(0.3)
    vaccinationValues.append(0.5)
    count = 0
    dsnSimulation = DSNSimulation()
    while count < dsnSimulation.runtime:
	graphStatistic = GraphStatistics()
	graphStatistic.resetStatistics()
	dsnSimulation.graphStatistics.append(graphStatistic)
	count += 1
    count = 0
    while count < 4:
        statistics.append(dsnSimulation.graphStatistics);
	count += 1
    count = 0
    while count < numberOfRunthroughs:
	cases = 0
	dsnSimulation.initializeSimulation(0.002167)
	tempGraph = copy.deepcopy(dsnSimulation.network)
	while cases < 4:
	    dsnSimulation.network = copy.deepcopy(tempGraph)
	    dsnSimulation.network.infectedNodes = set()
            dsnSimulation.network.varyingSusceptibilityNodes = set()
            dsnSimulation.network.loopListVariable = set()
	    dsnSimulation.graphStatistics = copy.deepcopy(statistics[cases])
	    dsnSimulation.initializeSimulation2(vaccinationValues[cases])
	    dsnSimulation.runSimulation()
	    dsnSimulation.endSimulation()
	    statistics[cases] = copy.deepcopy(dsnSimulation.graphStatistics)
	    cases += 1
	count += 1

    json_outfile = open('stats0.json', 'w')
    json.dump(statistics[0], json_outfile, default=GraphStatistics_encoder, indent=4)
    json_outfile.write("\n")
    json_outfile.close()
    json_outfile = open('stats1.json', 'w')
    json.dump(statistics[1], json_outfile, default=GraphStatistics_encoder, indent=4)
    json_outfile.write("\n")
    json_outfile.close()
    json_outfile = open('stats2.json', 'w')
    json.dump(statistics[2], json_outfile, default=GraphStatistics_encoder, indent=4)
    json_outfile.write("\n")
    json_outfile.close()
    json_outfile = open('stats3.json', 'w')
    json.dump(statistics[3], json_outfile, default=GraphStatistics_encoder, indent=4)
    json_outfile.write("\n")
    json_outfile.close()


    #total.append({'recoveryRate' : (loop * 100.00), 'totalInfected' : (dsnSimulation.totalInfected / numberOfRunthroughs)})
    #loop += 0.002

    #json_outfile = open('recovery.json', 'w')
    #json.dump(total, json_outfile, indent=4)
    #json_outfile.write("\n")
    #json_outfile.close()

    #json_outfile = open('stats.json', 'w')
    #json.dump(dsnSimulation.graphStatistics, json_outfile, default=GraphStatistics_encoder, indent=4)
    #json_outfile.write("\n")
    #json_outfile.close()

    #print("\n\nWrote statistics to " + json_outfile.name + "\n\n")
