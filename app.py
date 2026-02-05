# EJERCICIO 02.1 - Create a Script
print("Hello World")

# EJERCICIO 02.2 - Import
import pandas as pd
data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
print(data_frame)

# EJERCICIO 04 - Series
data = pd.Series([1, 94, 85, 31, 23, 8])
print(data)
edades = [23,45,7,34,6,63,36,78,54,34]
serie = pd.Series(edades)
print(serie)

# EJERCICIO 04.1 - Data Range
fechas = pd.date_range(start="2021-05-01", end="2021-05-12")
print(fechas)

# EJERCICIO 04.2 - Series Apply
my_series = pd.Series([2, 4, 6, 8, 10])
dividir = my_series.apply(lambda x: x / 2)
print(dividir)

# EJERCICIO 05 - DataFrames
data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
df = pd.DataFrame(data, columns=["Brand", "Model", "Color"])
print(df)

# EJERCICIO 05.1 - DataFrame Dict
data_dict = [
    { 
        "brand": "Toyota", 
        "model": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "model": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porsche", 
        "model": "Cayenne",
        "color": "White"
    },
    {
        "brand": "Tesla", 
        "model": "Model S",
        "color": "Red"
    }
]
df = pd.DataFrame(data_dict, columns=["brand", "model", "color"])
print(df)

# EJERCICIO 05.2 - DataFrame iLoc
import pandas as pd
data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
print(data_frame)
# DataFrame iLoc
print(data_frame.iloc[133,6])

# EJERCICIO 05.3 - DataFrame Head
import pandas as pd
data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
print(data_frame)
# DataFrame Head
print(data_frame.head(3))

# EJERCICIO 05.4 - DataFrame Tail
import pandas as pd
data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
print(data_frame)
# DataFrame Tail
print(data_frame.tail(3))

# EJERCICIO 05.5 - Print Columns
import pandas as pd
data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
print(data_frame)
# Print Columns
print(data_frame[['Name', 'Type 1']].head(10))

# EJERCICIO 05.6 - Loc Function
import pandas as pd
data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
print(data_frame)
# Loc Function
print(data_frame.loc[data_frame['Attack'] > 80])

# EJERCICIO 05.7 - Filter and Count
import pandas as pd
data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
print(data_frame)
# Filter and Count
legendary_pokemon = len(data_frame.loc[data_frame['Legendary'] == True])
print(legendary_pokemon)

# EJERCICIO 06 - Clean Datasets
import pandas as pd
data_frame = pd.read_csv(".learn/assets/us_baby_names_right.csv")
print(data_frame.head(5))

# EJERCICIO 06.1 - Remove Column
import pandas as pd
data_frame = pd.read_csv(".learn/assets/us_baby_names_right.csv")
print(data_frame.head(5))
del data_frame["Unnamed: 0"]
print(data_frame.head(5))

# EJERCICIO 06.2 - Value Counts
import pandas as pd
data_frame = pd.read_csv(".learn/assets/us_baby_names_right.csv")
print(data_frame.head(5))
# Value Counts
resultado = data_frame.value_counts("Gender")
print(resultado)

# EJERCICIO 06.3 - Group By
import pandas as pd
data_frame = pd.read_csv(".learn/assets/us_baby_names_right.csv")
print(data_frame.head(5))
# Value Counts
result = data_frame.groupby(by=["Name"]).sum()
print(len(result))
