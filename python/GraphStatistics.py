#!/usr/bin/env python
# -*- coding: utf-8 -*-

def GraphStatistics_encoder(obj):
    if isinstance(obj, GraphStatistics):
        return { 'timeInstant':obj.timeInstant,
                 'numberOfInfectedNodes' : obj.numberOfInfectedNodes,
                 'numberOfNewlyInfectedNodes' : obj.numberOfNewlyInfectedNodes,
                 'numberOfRecoveredNodes' : obj.numberOfRecoveredNodes,
		 'numberOfNodesInfectedByDispersion' : obj.nodesInfectedByDispersionEffect,
        }

    raise TypeError(repr(obj) + " is not JSON serializable")

class GraphStatistics(object):

    def __init__(self):
        timeInstant = 0
        numberOfInfectedNodes = 0
        numberOfNewlyInfectedNodes = 0
        numberOfRecoveredNodes = 0
	nodesInfectedByDispersionEffect = 0

    def displayStatistics(self):
        print "---------- STATISTICS FOR TIME INSTANT : " , self.timeInstant , " ---------"
        print "Number of infected nodes               : " , self.numberOfInfectedNodes
        print "Number of nodes infected by dispersion : " , self.nodesInfectedByDispersionEffect
        print "Number of newly infected nodes         : " , self.numberOfNewlyInfectedNodes
        print "Number of recovered nodes              : " , self.numberOfRecoveredNodes

    def resetStatistics(self):
        self.timeInstant = 0
        self.numberOfInfectedNodes = 0
        self.numberOfRecoveredNodes = 0
	self.nodesInfectedByDispersionEffect = 0


