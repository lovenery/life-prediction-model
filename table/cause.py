import pandas as pd
import os.path as path

df = pd.read_csv(path.join(path.dirname(__file__), './cause.csv'))

# print df

#.js
# for index, row in df.iterrows():
#     icd = row.icd.replace('/', ',')
#     print("{\n\tid: %d,\n\tname: \"%s\",\n\ticd: \"%s\"\n}," % (index+1, row.chinese, icd))

# .json
s = '['
nrows = df.shape[0]
for index, row in df.iterrows():
    icd = row.icd.replace('/', ',')
    s += ( "{\n\t\"id\": %d,\n\t\"name\": \"%s\",\n\t\"icd\": \"%s\"\n}" % (row.cause, row.chinese, icd) )
    if index+1 == nrows:
        break
    s += ",\n"
s += ']'
print s
# text_file = open(path.join(path.dirname(__file__), './cause.json'), "w")
# text_file.write(s)
# text_file.close()