# Import pandas as pd
import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


## functions
def filtergeneration(data, generation=1, onlySpecificGeneration=False):
    """Filtering the pokemons on generation
    In first regard will go up to specific generation. But can also select a specific gen
    """
    if onlySpecificGeneration:
        data = data[data["Generation"] == generation]
    else:
        data = data[data["Generation"] <= generation]
    return data


def filterlegendary(data, legendary=False):
    """if True -> will keep only legendary pokemons over"""
    if legendary:
        data = data[data["Legendary"]]
    return data


def filterstarter(data, starter=False):
    """if True -> will keep only starter pokemons over"""
    if starter:
        data = data[data["Starter"]]
    return data


# filter out types
def filterPokemonTypes(data, typeToFilterout=""):
    """can filter out a specific type of pokemon if not enering an empty string"""
    if typeToFilterout:
        data = data[
            np.logical_or(data["Type1"] == typeToFilterout, data["Type2"] == typeToFilterout)]
    return data


# handeling the mega evolutions
def handelingMegas(data, filterOutMegaEvolutions=False, keepOnlyMegaEvolutions=False):
    """In first instance made it so that mega's are filtered out because added late and are usually only interested in first gen
    But made setup so that can be kept in the general data or that only the megas are left
    """
    if filterOutMegaEvolutions:
        for lab, row in data.iterrows():
            data.loc[lab, "Mega"] = "Mega_" in str(row["Name"])
        data = data[data["Mega"] == keepOnlyMegaEvolutions]

    return data


# path to the file
mypath = Path().parent.absolute()
reletivePath = "/../../resources/csvfiles/pokemon.csv"

primeTypes = {'Bug': 'lightgreen', 'Dark': 'violet', 'Dragon': 'gold', 'Electric': 'orange', 'Fairy': 'darkviolet',
              'Fighting': 'red', 'Fire': 'red', 'Flying': 'lightblue', 'Ghost': 'violet', 'Grass': 'darkgreen',
              'Ground': 'brown', 'Ice': 'cyan', 'Normal': 'khaki', 'Poison': 'purple', 'Psychic': 'fuchsia',
              'Rock': 'maroon', 'Steel': 'grey', 'Water': 'blue'}

# Fix import by including index_col
pokemonData = pd.read_csv(str(mypath) + reletivePath)  # , index_col=0)

# filters generation, Legendary, starter
pokemonData = filtergeneration(pokemonData, 1, onlySpecificGeneration=True)
pokemonData = filterstarter(pokemonData, False)
pokemonData = filterlegendary(pokemonData, False)

pokemonData = filterPokemonTypes(pokemonData, "")

pokemonData = handelingMegas(pokemonData, filterOutMegaEvolutions=True, keepOnlyMegaEvolutions=False)

# Can select out: HP,Attack,Defense,Sp._Atk,Sp._Def,Speed
title = ""
size = "HP"
x = 'Attack'
y = 'Defense'

# datasetup
sizeFormat = np.array(pokemonData[[size]])
xValues = np.array(pokemonData[[x]])
yValues = np.array(pokemonData[[y]])

# finding types:
types = np.array(pokemonData[["Type1"]])[:, 0]

"""Colors are depended on the type 01 element (taking as 'assumption' that is is the 'main type') """
coloredtypes = np.vectorize(primeTypes.get)(types)

# plotting something
plt.scatter(xValues, yValues, s=sizeFormat, alpha=0.8, c=coloredtypes)
plt.xlabel(x)
plt.ylabel(y)
plt.title(title + x + "/" + y + " distribution")

names = np.array(pokemonData[["Name"]])[:, 0]

for i, txt in enumerate(names):
    plt.annotate(txt, (xValues[i], yValues[i]))

# show
plt.grid(True)
plt.show()
plt.clf()
