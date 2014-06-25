#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Config import Config
from Node import Node

class Network(object):

    def __init__(self):
	self.config = Config()
	self.graph = {}
	self._initializeNetwork()

    def _initializeNetwork(self):
	print "Initializing network"
	current_node=0
	while current_node < self.config.TOTAL_NODES:
	    self.graph[current_node] = Node()
	    current_node += 1
	print "Finished initializing network"

