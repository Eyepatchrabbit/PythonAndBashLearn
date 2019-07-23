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
# types = np.unique(np.array(pokemonData[["Type1"]]))
# print(types)=>set to color
primeTypes = {'Bug': '', 'Dark': '', 'Dragon': '', 'Electric': '', 'Fairy': '', 'Fighting': '', 'Fire': '', 'Flying': '',
         'Ghost': '', 'Grass': '', 'Ground': '', 'Ice': '', 'Normal': '', 'Poison': '', 'Psychic': '', 'Rock': '', 'Steel': '',
         'Water': ''}


# plotting something
plt.scatter(attack, defence, s=hp, alpha=0.8)
plt.xlabel('attack')
plt.ylabel('defence')
plt.title('attack/defence distribution')

# show
plt.grid(True)
plt.show()
