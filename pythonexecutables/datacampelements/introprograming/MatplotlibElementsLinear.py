# import matplotlib

import matplotlib.pyplot as plt

# Data Visualization is a key skill for aspiring data scientists.
# Matplotlib makes it easy to create meaningful and insightful plots.

year = [1950, 1970, 1990, 2010]
population = [2.519, 3.692, 5.263, 6.972]

# linear plot:
# =>time related (ordered over time!)
plt.plot(year, population)  # x,y

#lables
plt.xlabel("year")
plt.ylabel("Population (billion)")
plt.title("population projection")

#ticks
plt.yticks([0,2,3,4,5,6,7],["0","2*10^9","3*10^9","4*10^9","5*10^9","6*10^9","7*10^9"]) #set custom intervals for the axes


#customisations=>dependend on data and story to tell

plt.show()
