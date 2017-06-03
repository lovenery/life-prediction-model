import pandas as pd
import os.path as path

data = pd.read_csv(path.join(path.dirname(__file__), './data.csv'))
county = pd.read_csv(path.join(path.dirname(__file__), '../table/county.csv'))
# print data

county = county.reset_index()
result = pd.merge(data, county, on='county')
# print result

Z = pd.DataFrame()
Z['county'] = result['index'] + 1
Z['sex'] = result['sex']
Z['cause'] = result['cause']
Z['age'] = result['age']
# print Z
Z.to_csv(path.join(path.dirname(__file__), './result.csv'), index=False)
