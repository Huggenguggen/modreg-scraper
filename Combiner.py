import json
import pandas as pd
import numpy as np

def collate(output_filename, input_filenames):
  global df 
  first = True
  for infile_name in input_filenames:
    file = open(infile_name)
    data = json.load(file)
    temp_df = pd.json_normalize(data)
    temp_df.drop('index', inplace=True, axis=1)
    temp_df['Demand/Vacancy'] = (round((temp_df['Demand'].astype(np.integer) / temp_df['Vacancy'].astype(np.integer)), 2))
    temp_df['Demand/Vacancy'] = temp_df['Demand/Vacancy'].apply(np.array)
    temp_df.drop('Demand', inplace=True, axis=1)
    temp_df.drop('Vacancy', inplace=True, axis=1)
    #print(temp_df)
    if first:
      df = temp_df
      first = False
    else:
      for index, row in temp_df.iterrows():
        if row['Module\rCode'] in df['Module\rCode']:
          df.loc(row['Module\rCode'])['Demand\Vacancy'] = np.array(df.loc(row['Module\rCode'])['Demand\Vacancy']) + np.array(row['Demand\Vacancy'])
        else:
          df.append(row)
  print(df)
  return df.to_json(output_filename, orient="table")

res = collate('test.json', [r'Collated\Round0\20212022S2R0.json', r'Collated\Round0\20222023S1R0.json'])

          
            