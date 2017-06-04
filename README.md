# Life Prediction Model

## Env

- python 2.7

## Preparing Data

```shell
# merge data to merged.csv
python data/1-merge.py

# normalize data to data.csv (more than one hour)
python data/2-itertuples.py

# join data to result.csv
python data/3-county.py
```

## Development

```shell
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python model.py
export PORT=5000 # default: 5000
export FLASK_DEBUG=1 # debugger
python web/main.py
```
