# import matplotlib

import matplotlib.pyplot as plt

# Data Visualization is a key skill for aspiring data scientists.
# Matplotlib makes it easy to create meaningful and insightful plots.

year = [1950, 1970, 1990, 2010]
population = [2.519, 3.692, 5.263, 6.972]

#linear plot:
plt.plot(year, population)  # x,y
plt.show()

#scatter plot
plt.scatter(year, population)  # x,y
plt.show()

