#!/usr/bin/env python
# -*- coding: utf-8 -*-

from network import Network
from log import configure_logger 

def main():
    configure_logger()
    network = Network()

if __name__ == '__main__':
    main()


