from section2.optimisation import calculate_cost
from section2.optimisation import calculate_total_cost_polars
import pandas as pd
import numpy as np
import time

def generate_data(n):
    return pd.DataFrame({
        "status": np.random.choice(["active", "closed"], n),
        "currency": np.random.choice(["EUR", "USD"], n),
        "monthly_payment": np.random.randint(100, 1000, n),
        "asset_type": np.random.choice(["CAR", "FLEET", "OTHER"], n)
    })

def calculate_total_cost(df):
    results = []
    for _, row in df.iterrows():
        if row['status'] == 'active' and row['currency'] == 'EUR':
            cost = row['monthly_payment'] * 12
            if row['asset_type'] == 'CAR':
                cost *= 0.95  # 5% discount
            elif row['asset_type'] == 'FLEET':
                cost *= 0.90  # 10% discount
        else:
            cost = 0
        results.append(cost)
    df['annual_cost'] = results
    return df

def benchmark():
    print("Generating data...")
    df = generate_data(5000000)

    # ORIGINAL
    start = time.time()
    calculate_total_cost(df.copy())
    end = time.time()
    print("Original (loop):", end - start)

    # PANDAS
    start = time.time()
    calculate_cost(df.copy())
    end = time.time()
    print("Pandas (vectorized):", end - start)

    # POLARS
    start = time.time()
    calculate_total_cost_polars(df.copy())
    end = time.time()
    print("Polars:", end - start)

if __name__ == "__main__":
    benchmark()
