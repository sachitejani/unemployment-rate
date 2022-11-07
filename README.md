

# unemployment-rate



## Setup

Create and activate a virtual environment:

```sh
conda create -n unemployment-env python=3.8

conda activate unemployment-env
```

Install package dependencies:
```sh
pip install -r requirements.txt
```

## Configuration


[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Then create a local ".env" file and provide the key like this:

```sh
# this is the ".env" file...

API_KEY="_________"
```

## Usage

Run an example file 

```sh
python app/my_script.py
```

Run the unemployment report

```sh
# python app/unemployment.py
python -m app.unemployment
```

Run stocks report:

```sh
# python app/stocks.py - this is not modular
python -m app.stocks
```

## Testing

Run tests:

```sh
pytest
```