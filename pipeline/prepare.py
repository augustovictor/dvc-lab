import json

import pandas as pd
import yaml

data = pd.read_csv("./data/MOCK_DATA.csv")

print(data.info)

SUMMARY_FILE_NAME = "summary.json"


with open("params.yaml", 'r') as fd:
    params = yaml.safe_load(fd)

chosen_letter = params['prepare']['initial_letter_to_filter_for']


print(f"RESULTS FOR NAMES STARTING WITH LETTER {chosen_letter.upper()}")

result = data[data['first_name'].str.startswith('H')]

print(result.head())

with open(SUMMARY_FILE_NAME, 'w') as f:
    json.dump({'initial_letter_to_filter_for': chosen_letter}, f)
