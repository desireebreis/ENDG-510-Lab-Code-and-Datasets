import pandas as pd
import random as rand

df = pd.read_csv('T:/Uni/Final year/Digital/data.csv')

new_df = pd.DataFrame()

for i in range(30):

    new_data = {
        'Temp': rand.randint(0,100),
        'Humd': rand.randint(0,100),
        'Label': 0
    }

    new_df = new_df._append(new_data, ignore_index=True)

df = df._append(new_df, ignore_index=True)

df.to_csv("data_modified.csv", index=False)