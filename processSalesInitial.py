#!/usr/bin/env python
__author__ = "Arana Fireheart"

filename = "salesData.txt"
salesData = {}

with open(filename, 'r') as salesInput:
    header = salesInput.readline()
    for line in salesInput.readlines():
        if len(line.strip()) > 0:
            itemName, totalSalesQuantity, piecePrice = line.strip().split('\t')
            salesData[itemName] = totalSalesQuantity
pass