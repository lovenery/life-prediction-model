# Life Prediction Model

## ENV

- python 2.7

## Preparing Data

```shell
# merge data to merged.csv
python data/1-merge.py

# normalize data (more than one hour)
python data/2-itertuples.py

# join data
python data/3-county.py
```

## Run

```shell
# make model, output file: rfc.pkl
python model.py

# run web service
python web/main.py
```
