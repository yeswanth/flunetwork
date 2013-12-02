#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

class Node(object):

    def __init__(self):
        self.susceptibility = random.randrange(35) / 1000.00 + 0.016
        self.currentSusceptibility = self.targetSusceptibility = self.susceptibility
        self.infected = False
        self.vaccineEffectCompleted = True
        self.infectionTime = 0
        self.neighbours = set()
        self.infectionTime = 0
        self.vaccineEffectiveness = 0.7
        self.infectionImmunity = 0.7
        self.susceptibilityRecoveryValue = 0.003
        self.recoveryTime = 5
        self.vaccineEffectPeriod = 14
        print("Value of susceptibility for node = " , self.susceptibility)

    def vaccinate(self):
        self.vaccineEffectCompleted = False
        self.targetSusceptibility = self.susceptibility * (1.0 - self.vaccineEffectiveness)

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
        if self.infected:
            return False
        if random.randrange(1001) / 1000.00 < self.currentSusceptibility:
            self.infected = True
            self.infectionTime = 0
            return True
        return False

    def isRecovered(self):
        if not self.infected:
            return False
        self.infectionTime += 1
        if self.infectionTime < self.recoveryTime:
            return False
        self.infected = False
        self.resetInfection()
        return True

    def resetInfection(self):
        self.infectionTime = 0
        self.currentSusceptibility = self.currentSusceptibility * 1.0 - self.infectionImmunity
        self.targetSusceptibility = self.susceptibility
        self.vaccineEffectCompleted = True


