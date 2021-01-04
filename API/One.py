# api is a tool for you to get information from a database or a service
import requests as re
from random import *


# url : https://randomfox.ca/
# api url : https://randomfox.ca/floof
response = re.get("https://randomfox.ca/floof")
# print(response.status_code)
# print(response.text) # this is a STRING, not a dictionary
# print(response.json()) # this is a DICTIONARY, not a string
fox = response.json()



