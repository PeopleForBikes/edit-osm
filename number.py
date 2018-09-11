# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 15:30:17 2018

@author: rebec
"""

from lxml import etree

# default path
fpath = "C://users/rebec/documents/osm/test/"

#  read osm file
tree = etree.parse(fpath + 'helvetia_mod.osm')

# identify nodes with negative id
ways = tree.xpath('.//way[starts-with(@id, "-")]')

# identify ways with negative id
nodes = tree.xpath('.//node[starts-with(@id, "-")]')

# identify refs with negative id
# refs = tree.xpath('.//nd[starts-with(@ref, "-")]')

# Set root, which is OSM tag
root = tree.getroot()

## WAYS
ways_len = len(ways)

while ways_len > 0:    
    root.insert(root.index(ways[0]), ways[ways_len-1])
    ways_len-=1

## NODES
nodes_len = len(nodes)

while nodes_len > 0:    
    root.insert(root.index(nodes[0]), nodes[nodes_len-1])
    nodes_len-=1
    
# Write to file
tree.write(fpath + 'newxml.osm', pretty_print=True, xml_declaration=True, encoding="utf-8")
