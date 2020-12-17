#!/usr/bin/env python
__author__ = "Arana Fireheart"

from matplotlib.pyplot import rcdefaults, subplots, show
import numpy

# Fixing random state for reproducibility
numpy.random.seed(19680801)


rcdefaults()
fig, ax = subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
yPosition = numpy.arange(len(people))
performance = 3 + 10 * numpy.random.rand(len(people))
error = numpy.random.rand(len(people))

ax.bar(yPosition, performance, xerr=error, align='center')
ax.set_xticks(yPosition)
ax.set_xticklabels(people)
# ax.invert_yaxis()  # labels read top-to-bottom
ax.set_ylabel('Performance')
ax.set_title('How fast do you want to go today?')

show()
pass