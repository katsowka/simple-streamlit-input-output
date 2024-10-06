import numpy as np
import pandas as pd

df = pd.read_csv("insurance_data.csv", index_col=0) 

# for inputs:
regions = list(df['region'].unique()) 
min_age = df['age'].min()
max_age = df['age'].max()

# for output:
def get_mean_claim(selected_region: str, selected_age: int) -> tuple[int, float]:
    filter_region = df['region'] == selected_region
    filter_age = df['age'] == selected_age
    num_claims = len(df[(filter_region & filter_age)])
    mean_claim = df[(filter_region & filter_age)]['claim'].mean()
    return (num_claims, mean_claim)