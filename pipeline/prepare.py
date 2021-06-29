import pandas as pd
import yaml

from utils.utils import save_metrics

data = pd.read_csv("./data/MOCK_DATA.csv")

print(data.info)

with open("params.yaml", 'r') as fd:
    params = yaml.safe_load(fd)

chosen_letter = params['prepare']['initial_letter_to_filter_for']


print(f"RESULTS FOR NAMES STARTING WITH LETTER {chosen_letter.upper()}")

result = data[data['first_name'].str.startswith('H')]

print(result.head())

save_metrics({'initial_letter_to_filter_for': chosen_letter})
