# https://pandas.pydata.org/pandas-docs/stable/merging.html
import pandas as pd
import os.path as path

def start():
    frames = []
    for i in range(0, 5): # 0~4
        filename = 'dead10' + str(i) + '.csv'
        print('Appending...' + filename)
        df = pd.read_csv(path.join(path.dirname(__file__), filename))
        frames.append(df)

    df = pd.concat(frames)
    # print(df.head())
    print('Append Done!\n')

    df.to_csv(path.join(path.dirname(__file__), './merged.csv'), index=False)

if __name__ == '__main__':
    start()