import pandas as pd
import os.path as path

df = pd.read_csv(path.join(path.dirname(__file__), './county.csv'))

# print df

# .js
for index, row in df.iterrows():
    print("{\n\tid: %d,\n\tname: \"%s\"\n}," % (index+1, row.chinese))
