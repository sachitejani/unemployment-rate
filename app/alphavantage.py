# This is the alphavantage file

import os
from dotenv import load_dotenv

load_dotenv() # look in the ".env" file for env vars

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")