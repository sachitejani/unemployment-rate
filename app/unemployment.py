
# this is the "app/unemployment_report.py" file...

import os
import json
from pprint import pprint

import requests

API_KEY = os.getenv("API_KEY")

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)
print(type(parsed_response))
pprint(parsed_response)

#breakpoint()

latest = parsed_response["data"][0]
print(latest)