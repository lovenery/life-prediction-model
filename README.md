# Life Prediction Model

## Env

- python 2.7

## Preparing Data

```shell
# merge data to merged.csv
python data/1-merge.py

# normalize data (more than one hour)
python data/2-itertuples.py

# join data
python data/3-county.py

# make model, output file: *.pkl
python model.py
```

## Development

```shell
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python model.py
export PORT=5000
python web/main.py
```
