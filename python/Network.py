#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Config import *
from Node import Node

class Network(object):

    def __init__(self):
	self.graph = {}
	self._initializeNetwork()

    def _initializeNetwork(self):
	print "Initializing network"
	current_node=0
	while current_node < TOTAL_NODES:
	    self.graph[current_node] = Node()
	    current_node += 1
	print "Finished initializing network"

