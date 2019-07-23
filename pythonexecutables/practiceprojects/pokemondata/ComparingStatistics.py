# Import pandas as pd
import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# path to the file
mypath = Path().parent.absolute()
reletivePath = "/../../resources/csvfiles/pokemon.csv"

# Fix import by including index_col
pokemonData = pd.read_csv(str(mypath) + reletivePath, index_col=0)

# print(pokemonData)

# datasetup
hp = np.array(pokemonData[["HP"]])
attack = np.array(pokemonData[['Attack']])
defence = np.array(pokemonData[['Defense']])

# finding types:
types = np.array(pokemonData[["Type1"]])
# print(types)=>set to color
primeTypes = {'Bug': 'lightgreen', 'Dark': 'darkviolet', 'Dragon': 'gold', 'Electric': 'orange', 'Fairy': 'violet',
              'Fighting': 'coral', 'Fire': 'red', 'Flying': 'deepskyblue', 'Ghost': 'lightgrey', 'Grass': 'green',
              'Ground': 'sandbrown', 'Ice': 'darkcyan', 'Normal': 'ivory', 'Poison': 'purple', 'Psychic': 'fuchsia',
              'Rock': 'maroon', 'Steel': 'grey', 'Water': 'blue'}

coloredtypes= np.array(np.vectorize(primeTypes.get)(types))
#print(coloredtypes)

# plotting something
plt.scatter(attack, defence, s=hp, alpha=0.8)#,c=coloredtypes)
plt.xlabel('attack')
plt.ylabel('defence')
plt.title('attack/defence distribution')

# show
plt.grid(True)
plt.show()
