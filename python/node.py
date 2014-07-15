#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from config import MEAN_NEIGHBOURS, STANDARD_DEVIATION 

class Node(object):

    def __init__(self):
	print "Initializing node"
	self.no_of_neighbours = MEAN_NEIGHBOURS + random.randrange(STANDARD_DEVIATION*2) - STANDARD_DEVIATION
	print "Maximum number of neighbours for node = ", self.no_of_neighbours
	self.neighbours = set()

