import pandas as pd
import os

data={'Name': ['Alice', 'Bob', 'Charlie'],
      'Age': [25, 30, 35],
      'City': ['New York', 'Los Angeles', 'Chicago']}

df=pd.DataFrame(data)

new_roc_loc={'Name': 'salman','Age': 28,'City': 'San Francisco'}

df.loc[len(df.index)] = new_roc_loc

new_roc_loc={'Name': 'hammad','Age': 22,'City': 'abtd'}

df.loc[len(df.index)] = new_roc_loc

data_dir='data'
os.makedirs(data_dir, exist_ok=True)
file_path=os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)
print(f"DataFrame saved to {file_path}")