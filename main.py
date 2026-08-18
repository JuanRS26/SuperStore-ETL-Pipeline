import scripts.explorer_data  as ed
import pandas as pd

# Se exportan los datos
df = pd.read_csv('data/raw/samplesuperstore.csv')

# ed.exploration(df)

print(df[df['Customer ID'] == 'WB-21850'][['Row ID', 'Order ID', 'Customer ID', 'Customer Name', 'City', 'State/Province', 'Segment']])



          





