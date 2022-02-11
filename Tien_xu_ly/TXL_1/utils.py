# import pandas as pd
import random

def get_random_row(df, size=20):
    max_random = df.shape[0] - size
    start_idx = random.randint(0, max_random)
    return df[start_idx:start_idx + size]