import pandas as pd

df = pd.read_csv(r'/workspaces/Danske-data-assignment/section1/loan_agreement.csv')

# print(df)
# print(df.dtypes)

def clean_agreements(df):
    df['currency'] = df['currency'].str.upper()
    df['status'] = df['status'].str.lower()   
    df['start_date_parsed'] = pd.to_datetime(df["start_date"], errors="coerce")
    df['end_date_parsed'] = pd.to_datetime(df["end_date"], errors="coerce")
    df['has_date_error'] = df['start_date_parsed'].isna() | df['end_date_parsed'].isna()
    df['has_date_logic_error'] = (df['end_date_parsed'] <= df['start_date_parsed']) & ~df['has_date_error']
    df['has_payment_error'] = df['monthly_payment'] <= 0
    df['customer_id'] = df['customer_id'].fillna('UNKNOWN')
    return df

df_clean = clean_agreements(df)
print(df_clean)

# print(df_clean.dtypes)

def summarise_errors(df: pd.DataFrame) -> dict:
    error_summary = {
        'has_date_error': df['has_date_error'].sum(),
        'has_date_logic_error': df['has_date_logic_error'].sum(),
        'has_payment_error': df['has_payment_error'].sum()
    }
    return error_summary
    

summary = summarise_errors(df_clean)
print(summary)