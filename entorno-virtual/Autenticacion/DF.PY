import pandas as pd

# Lee el archivo de Excel
# Guarda el DataFrame en un archivo de Excel
df = pd.read_excel('DataEmpeloyes#2.xlsx')
la = df.to_excel('DataEmpeloyes#2.xlsx', index=False)
