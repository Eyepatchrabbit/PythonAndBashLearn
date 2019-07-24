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
types = np.array(pokemonData[["Type1"]])[:,0]
primeTypes = {'Bug': 'lightgreen', 'Dark': 'violet', 'Dragon': 'gold', 'Electric': 'orange', 'Fairy': 'darkviolet',
              'Fighting': 'red', 'Fire': 'red', 'Flying': 'lightblue', 'Ghost': 'violet', 'Grass': 'darkgreen',
              'Ground': 'brown', 'Ice': 'cyan', 'Normal': 'ivory', 'Poison': 'purple', 'Psychic': 'fuchsia',
              'Rock': 'maroon', 'Steel': 'grey', 'Water': 'blue'}

coloredtypes =np.vectorize(primeTypes.get)(types)


# plotting something
plt.scatter(attack, defence, s=hp, alpha=0.8 , c=coloredtypes)
plt.xlabel('attack')
plt.ylabel('defence')
plt.title('attack/defence distribution')

names = np.array(pokemonData[["Name"]])[:,0]

#for i, txt in enumerate(names):
#    plt.annotate(txt, (attack[i], defence[i]))

# show
plt.grid(True)
plt.show()
