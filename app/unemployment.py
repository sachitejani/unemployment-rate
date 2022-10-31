
# this is the "app/unemployment_report.py" file...

import json
from pprint import pprint
import requests
from statistics import mean
from app.alphavantage import API_KEY

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)
# print(type(parsed_response))
# pprint(parsed_response)

#breakpoint()


# Part A
latest = parsed_response["data"][0]
latest_value = latest["value"]
latest_date = latest["date"]

print("-------------------------")
print("LATEST UNEMPLOYMENT RATE:")
print(f"{latest_value}%", "as of", latest_date)

# Part B
 
this_year = [d for d in parsed_response["data"] if "2022-" in d["date"]]
 
rates_this_year = [float(d["value"]) for d in this_year]
#print(rates_this_year)
 
print("-------------------------")
print("AVG UNEMPLOYMENT THIS YEAR:", f"{mean(rates_this_year)}%")
print("NO MONTHS:", len(this_year))

 
# Part C
 
from plotly.express import line
 
dates = [d["date"] for d in parsed_response["data"]]
rates = [float(d["value"]) for d in parsed_response["data"]]
 
fig = line(x=dates, y=rates, title="United States Unemployment Rate over time", labels= {"x": "Month", "y": "Unemployment Rate"})
fig.show()


