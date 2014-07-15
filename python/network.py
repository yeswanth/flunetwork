#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import logging

from config import TOTAL_NODES, TOTAL_TRIES 
from node import Node

class Network(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)
	self.graph = {}
	self._initializeNetwork()

    def _initializeNetwork(self):
        self.logger.info("Initializing network")
	current_node = 0
	while current_node < TOTAL_NODES:
	    self.graph[current_node] = Node()
	    count = self.graph[current_node].no_of_neighbours
	    while count:
		tries = TOTAL_TRIES
		while tries:
		    tries -= 1
		    while True:
			neighbour = random.randrange(TOTAL_NODES);
			if neighbour != current_node:
			    break
		    if neighbour in self.graph and self.graph[neighbour] is not None:
			if current_node in self.graph[neighbour].neighbours:
			   continue
		    else:
			self.graph[neighbour] = Node()
		    
		    if not self.graph[neighbour].no_of_neighbours:
			continue

		    self.graph[current_node].neighbours.add(neighbour)
		    self.graph[neighbour].neighbours.add(current_node)
		    self.graph[neighbour].no_of_neighbours -= 1
		    self.graph[current_node].no_of_neighbours -= 1
                    self.logger.info("Adding link between %d and %d",current_node,neighbour)
		    break

		count -= 1
		
            self.logger.debug("Number of neighbours for node %d is = %d",current_node, 
                                    len(self.graph[current_node].neighbours))
	    current_node += 1
	    
        self.logger.info("Finished initializing network")

