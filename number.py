# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 15:30:17 2018

@author: rebec

When editing OpenStreetMap (OSM) data in JOSM, new features are tagged
with a negative ID number. The negative numbers are listed
with a decreasing value (e.g. -1, -3, -5). However the BNA
requires ID values to run in increasing order, (e.g. -5, -3, -1).
This script ingests a modified OSM file with negative ID values and 
reverses the order of the IDs for both nodes and ways.

Inputs: Modified OSM file
Outputs: Modified OSM file with numbers reordered by magnitude

"""
# Library to edit XML files
from lxml import etree
import os

# default path
fpath = os.getcwd()

#  read osm file
tree = etree.parse(fpath + 'helvetia_mod.osm')

# identify nodes with negative id
ways = tree.xpath('.//way[starts-with(@id, "-")]')

# identify ways with negative id
nodes = tree.xpath('.//node[starts-with(@id, "-")]')

# Set root, which is OSM tag
root = tree.getroot()

# function to resort nodes or ways
def reorder(osm_object, root):
    
    object_len = len(osm_object)
    
    if object_len <= 0:
        return
    while object_len > 0:
        root.insert(root.index(osm_object[0], osm_object[object_len-1]))    
        object_len-=1
    
# run reorder function for nodes and ways
reorder(nodes, root)
reorder(ways, root)

# Write to file
tree.write(fpath + '/revised_xml.osm', pretty_print=True, xml_declaration=True, encoding="utf-8")
