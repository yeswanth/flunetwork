#!/usr/bin/env python
# -*- coding: utf-8 -*-


class GraphStatistics(object):
    timeInstant = 0
    numberOfInfectedNodes = 0
    numberOfNewlyInfectedNodes = 0
    numberOfRecoveredNodes = 0

    def getTimeInstant(self):
        return self.timeInstant

    def setTimeInstant(self, timeInstant):
        self.timeInstant = self.timeInstant

    def getNumberOfInfectedNodes(self):
        return self.numberOfInfectedNodes

    def setNumberOfInfectedNodes(self, numberOfInfectedNodes):
        self.numberOfInfectedNodes = self.numberOfInfectedNodes

    def getNumberOfNewlyInfectedNodes(self):
        return self.numberOfNewlyInfectedNodes

    def setNumberOfNewlyInfectedNodes(self, numberOfNewlyInfectedNodes):
        self.numberOfNewlyInfectedNodes = self.numberOfNewlyInfectedNodes

    def getNumberOfRecoveredNodes(self):
        return self.numberOfRecoveredNodes

    def setNumberOfRecoveredNodes(self, numberOfRecoveredNodes):
        self.numberOfRecoveredNodes = self.numberOfRecoveredNodes

    def displayStatistics(self):
        print "---------- STATISTICS FOR TIME INSTANT : " , self.timeInstant , " ---------"
        print "Number of infected nodes       : " , self.numberOfInfectedNodes
        print "Number of newly infected nodes : " , self.numberOfNewlyInfectedNodes
        print "Number of recovered nodes      : " , self.numberOfRecoveredNodes

    def resetStatistics(self):
        self.timeInstant = 0
        self.numberOfInfectedNodes = 0
        self.numberOfRecoveredNodes = 0


