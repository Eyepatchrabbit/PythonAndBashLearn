# Import pandas as pd
import pandas as pd
from pathlib import Path

# path to the file
mypath = Path().parent.absolute()
reletivePath = "/../../resources/csvfiles/cars.csv"

# Fix import by including index_col
cars = pd.read_csv(str(mypath) + reletivePath, index_col=0)

# Print out cars
print(cars)

print("\n")

##printing based on column names
# Print out country column as Pandas Series
print("\ncountry column as Pandas Series")
print(cars["country"])  # not recomended !!!!
# Print out country column as Pandas DataFrame
print("\ncountry column as Pandas DataFrame")
print(cars[["country"]])
# Print out DataFrame with country and drives_right columns
print("\ncountry and drives_right columns")
print(cars[["country", "drives_right"]])

##printing based on row numbers
# Print out first 3 observations
print("\nPrint out first 3 observations")
print(cars[0:3])
# Print out fourth, fifth and sixth observation
print("\nfourth, fifth and sixth observation")
print(cars[3:6])

##loc & iloc
print("\nusing loc and Iloc=>more recomended!!!!\n")
print("\nusing loc")
# Print out observation for Japan
print("\nsingle quotes: \n", cars.loc['JAP'])  # as Serie
print("\ndouble quotes: \n", cars.loc[['JAP']])  # as DataFrame
# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])

print("\nusing iloc")
# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.iloc[[1, -1]])

# selecting specific rows and columns:
print("\nselecting specific rows and columns\n")
print("\n", cars.loc['IN', 'cars_per_cap'])
print("\n", cars.iloc[3, 0])
print("\n", cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']])
print("\n", cars.iloc[[3, 4], [0, 1]])
# Print out drives_right column as Series
print("\n", cars.loc[:, ['drives_right']])
# Print out drives_right column as DataFrame
print("\n", cars.loc[:, 'drives_right'])
