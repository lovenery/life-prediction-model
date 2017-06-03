import pandas as pd
import os.path as path

df = pd.read_csv(path.join(path.dirname(__file__), './age.csv'))

# print df

# .js
# for index, row in df.iterrows():
#     print("{\n\tid: %d,\n\tname: \"%s\"\n}," % (row.age_code, row.chinese))

# .json
s = '['
nrows = df.shape[0]
for index, row in df.iterrows():
    s += ( "{\n\t\"id\": %d,\n\t\"name\": \"%s\"\n}" % (row.age_code, row.chinese) )
    if index+1 == nrows:
        break
    s += ",\n"
s += ']'
print s
# text_file = open(path.join(path.dirname(__file__), './age.json'), "w")
# text_file.write(s)
# text_file.close()