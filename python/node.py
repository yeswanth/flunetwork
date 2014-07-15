#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import logging

from config import MEAN_NEIGHBOURS, STANDARD_DEVIATION 

class Node(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initializing node")
	self.no_of_neighbours = MEAN_NEIGHBOURS + random.randrange(STANDARD_DEVIATION*2) - STANDARD_DEVIATION
    
        self.logger.debug("Maximum number of neighbours for node = %d",self.no_of_neighbours)
	self.neighbours = set()

