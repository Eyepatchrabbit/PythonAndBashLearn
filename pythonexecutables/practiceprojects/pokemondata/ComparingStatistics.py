# Import pandas as pd
import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# path to the file
mypath = Path().parent.absolute()
reletivePath = "/../../resources/csvfiles/pokemon.csv"

# Fix import by including index_col
pokemonData = pd.read_csv(str(mypath) + reletivePath)#, index_col=0)

#filters generation, Legendary, starter
#pokemonData = pokemonData[pokemonData["Generation"] == 1]
#pokemonData = pokemonData[pokemonData["Legendary"]]
pokemonData = pokemonData[pokemonData["Starter"]]

#filter out types
#typeToFilterout = "Steel"
#pokemonData = pokemonData[np.logical_or(pokemonData["Type1"] == typeToFilterout, pokemonData["Type2"] == typeToFilterout)]

# filtering out mega's
for lab, row in pokemonData.iterrows():
   pokemonData.loc[lab, "Mega"] = "Mega_" in str(row["Name"])
pokemonData = pokemonData[pokemonData["Mega"] != True]

#HP,Attack,Defense,Sp._Atk,Sp._Def,Speed
x = 'Attack'
y = 'Defense'

# datasetup
hp = np.array(pokemonData[["HP"]])
attack = np.array(pokemonData[[x]])
defence = np.array(pokemonData[[y]])

# finding types:
types = np.array(pokemonData[["Type1"]])[:, 0]
primeTypes = {'Bug': 'lightgreen', 'Dark': 'violet', 'Dragon': 'gold', 'Electric': 'orange', 'Fairy': 'darkviolet',
              'Fighting': 'red', 'Fire': 'red', 'Flying': 'lightblue', 'Ghost': 'violet', 'Grass': 'darkgreen',
              'Ground': 'brown', 'Ice': 'cyan', 'Normal': 'khaki', 'Poison': 'purple', 'Psychic': 'fuchsia',
              'Rock': 'maroon', 'Steel': 'grey', 'Water': 'blue'}

coloredtypes = np.vectorize(primeTypes.get)(types)

# plotting something
plt.scatter(attack, defence, s=hp, alpha=0.8, c=coloredtypes)
plt.xlabel(x)
plt.ylabel(y)
plt.title('attack/defence distribution')

names = np.array(pokemonData[["Name"]])[:, 0]

for i, txt in enumerate(names):
    plt.annotate(txt, (attack[i], defence[i]))

# show
plt.grid(True)
plt.show()
