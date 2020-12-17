#!/usr/bin/env python
__author__ = "Arana Fireheart"

inputFilename = "salesData.txt"

highestSalesItem = ["", -1]
lowestSalesItem = ["", 9999999]
salesData = {}
with open(inputFilename, 'r') as inputData:
    header = inputData.readline()
    for line in inputData.readlines():
        if len(line.strip()) > 0:
            itemName, totalSalesQuantity, piecePrice = line.strip().split('\t')
            salesData[itemName] = [int(totalSalesQuantity), float(piecePrice)]

for itemName, (quantitySold, piecePrice) in salesData.items():
    if quantitySold > highestSalesItem[1]:
        highestSalesItem = [itemName, quantitySold]
    if quantitySold < lowestSalesItem[1]:
        lowestSalesItem = [itemName, quantitySold]

highestQuantity, highestPiecePrice = salesData[highestSalesItem[0]]

print(f"High: {highestSalesItem[1]} {highestSalesItem[0]}es were sold for ${highestQuantity * highestPiecePrice}")

lowestQuantity, lowestPiecePrice = salesData[lowestSalesItem[0]]

print(f"Low: {lowestSalesItem[1]} {lowestSalesItem[0]}s were sold for ${lowestQuantity * lowestPiecePrice}")
pass