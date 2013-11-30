#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node(object):
    """ generated source for Node

    """
    susceptibility = float()
    targetSusceptibility = float()
    currentSusceptibility = float()
    infected = bool()
    vaccineEffectCompleted = bool()
    infectionTime = 0
    vaccineEffectiveness = 0.7
    infectionImmunity = 0.7
    susceptibilityRecoveryValue = 0.003
    recoveryTime = 5
    vaccineEffectPeriod = 14

    def getSusceptibility(self):
        return self.susceptibility

    def setSusceptibility(self, susceptibility):
        self.susceptibility = self.susceptibility

    def getTargetSusceptibility(self):
        return self.targetSusceptibility

    def setTargetSusceptibility(self, targetSusceptibility):
        self.targetSusceptibility = self.targetSusceptibility

    def getCurrentSusceptibility(self):
        return self.currentSusceptibility

    def setCurrentSusceptibility(self, currentSusceptibility):
        self.currentSusceptibility = self.currentSusceptibility

    def isInfected(self):
        return self.infected

    def setInfected(self, infected):
        self.infected = self.infected

    def isVaccineEffectCompleted(self):
        return self.vaccineEffectCompleted

    def setVaccineEffectCompleted(self, vaccineEffectCompleted):
        self.vaccineEffectCompleted = self.vaccineEffectCompleted

    def getInfectionTime(self):
        return self.infectionTime

    def setInfectionTime(self, infectionTime):
        self.infectionTime = self.infectionTime

    def getNeighbours(self):
        return neighbours

    def setNeighbours(self, neighbours):
        self.neighbours = neighbours

    def __init__(self):
        random = Random()
        self.susceptibility = random.nextInt(35) / 1000.00 + 0.016
        self.currentSusceptibility = self.targetSusceptibility = self.susceptibility
        self.infected = False
        self.vaccineEffectCompleted = True
        self.infectionTime = 0
        print "Value of susceptibility for node = " + self.susceptibility

    def vaccinate(self):
        self.vaccineEffectCompleted = False
        self.targetSusceptibility = self.susceptibility * 1.0 - self.vaccineEffectiveness

    def updateSusceptibility(self):
        if not self.vaccineEffectCompleted:
            if self.currentSusceptibility > self.targetSusceptibility:
                self.currentSusceptibility -= self.susceptibility * self.vaccineEffectiveness / self.vaccineEffectPeriod
                return True
            self.vaccineEffectCompleted = True
            self.targetSusceptibility = self.susceptibility
        if self.currentSusceptibility < self.targetSusceptibility:
            self.currentSusceptibility += self.susceptibilityRecoveryValue
            if self.currentSusceptibility > self.targetSusceptibility:
                self.currentSusceptibility = self.targetSusceptibility
            return True
        return False

    def infect(self, globalDecayValue):
        if self.isInfected():
            return False
        if random.nextInt(1001) / 1000.00 < self.getCurrentSusceptibility():
            self.setInfected(True)
            self.setInfectionTime(0)
            return True
        return False

    def isRecovered(self):
        if not self.isInfected():
            return False
        self.infectionTime += 1
        if self.infectionTime < self.recoveryTime:
            return False
        self.setInfected(False)
        self.resetInfection()
        return True

    def resetInfection(self):
        self.infectionTime = 0
        self.currentSusceptibility = self.currentSusceptibility * 1.0 - self.infectionImmunity
        self.targetSusceptibility = self.susceptibility
        self.vaccineEffectCompleted = True


