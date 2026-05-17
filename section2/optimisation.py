from section2.pipeline import extract, engine
import polars as pl
import logging
#Extracting data from the database to do this exercise
df_data = extract(engine)
logging.info("Data extracted successfully for optimisation exercise.")

def calculate_cost(df_data):
    df_data['active_eur'] = (
        (df_data["currency"].str.upper() == "EUR") & (df_data["status"].str.upper() == "ACTIVE"))
    df_data['Cost'] = 0
    df_data.loc[df_data['active_eur'], 'Cost' ] = df_data['monthly_payment'] * 12
    df_data.loc[df_data['active_eur']  & (df_data['asset_type'] == "CAR"), 'Cost' ] *= 0.95
    df_data.loc[df_data['active_eur']  & (df_data['asset_type'] == "FLEET"), 'Cost' ] *= 0.90
    return df_data

logging.info("Cost calculation function defined successfully.")
calculate_cost(df_data)

# Optimised version using Polars

def calculate_total_cost_polars(df_data):
    lazy_df = pl.from_pandas(df_data).lazy()
    condition = (
        (pl.col("status").str.to_uppercase() == "ACTIVE") &
        (pl.col("currency").str.to_uppercase() == "EUR")
    )    
    lazy_df = lazy_df.with_columns(
        pl.when(condition)
        .then(
            pl.when(pl.col("asset_type") == "CAR")
            .then(pl.col("monthly_payment") * 12 * 0.95)

            .when(pl.col("asset_type") == "FLEET")
            .then(pl.col("monthly_payment") * 12 * 0.90)

            .otherwise(pl.col("monthly_payment") * 12)
        )
        .otherwise(0)
        .alias("Cost")
    )
    return lazy_df.collect().to_pandas()

calculate_total_cost_polars(df_data)

# Briefly explain (2–4 sentences) why the original implementation is slow and what makes your solution faster.

# The original code is slow because it goes through each row one by one using iterrows(), which takes a lot of time when the data is large.
# In the pandas version, instead of looping, we use column‑level operations, so the calculation happens on the entire column at once, which is much faster.
# In the Polars version, it is even faster because it uses lazy execution. It doesn’t run each step immediately, but builds the logic first and then executes it in an optimized way.
# This is similar to how PySpark works, where transformations are optimized before actual execution, which improves performance.