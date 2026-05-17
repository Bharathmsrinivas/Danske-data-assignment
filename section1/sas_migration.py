import pandas as pd

def calculate_risk_score(df: pd.DataFrame) -> pd.DataFrame:
    df_active = df[df['status'] == 'active'].copy()
    df_active_new = df_active.groupby('customer_id').agg(
        total_exposure = ('monthly_payment', 'sum'),
        agreement_count = ('monthly_payment', 'count')
    )
    df_active_new['avg_exposure'] = df_active_new['total_exposure'] / df_active_new['agreement_count']
    all_customers = pd.DataFrame({'customer_id': df['customer_id'].unique()})
    df_final = pd.merge(all_customers,df_active_new, on='customer_id', how='left')
    df_final['avg_exposure'] = df_final['avg_exposure'].fillna(0)
    return df_final

# df_risk = calculate_risk_score(df_clean)
# print(df_risk)