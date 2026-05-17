
from sqlalchemy import create_engine
import pandas as pd

import logging
logging.basicConfig(level=logging.INFO)
from section1.cleaning import clean_agreements
from section1.sas_migration import calculate_risk_score

engine = create_engine('sqlite:///agreements.db')

df = pd.DataFrame({
    "agreement_id": ["LN-001","LN-002","LN-003","LN-004","LN-005","LN-006","LN-007","LN-008"],
    "customer_id": ["C100","C101","C102","C100", None,"C104","C105","C106"],
    "asset_type": ["CAR","EQUIPMENT","FLEET","CAR","CAR","EQUIPMENT","FLEET","CAR"],
    "start_date": ["2022-01-15","","2021-03-01","2023-07-01","2022-11-01","2023-01-01","2023-05-01","not-a-date"],
    "end_date": ["2025-01-15","2024-06-01","2024-03-01","2026-07-01","2025-11-01","2022-01-01","2026-05-01","2025-09-01"],
    "monthly_payment": [450.00,1200.5,800,450.00,300.00,950.00,-200.00,560.00],
    "currency": ["EUR","eur","USD","EUR","EUR","EUR","EUR","EUR"],
    "status": ["active","ACTIVE","closed","active","active","active","active","active"]
})

#loading the data into the database
df.to_sql('agreements', engine, if_exists='replace', index=False)

#Extracting data from the database to verify the insertion
#Step 1 Extract
def extract(engine):
    df_raw = pd.read_sql('SELECT * FROM agreements', engine)
    # print(df_raw)
    logging.info("Data extracted successfully from the database.")
    return df_raw

#Step 2 Transform

def transform(df_raw):
    df_cleaned = clean_agreements(df_raw)
    # print(df_cleaned)
    logging.info("Data cleaning and data quality checks completed.")
    df_risk_score = calculate_risk_score(df_cleaned)
    # print(df_risk_score)
    logging.info("Risk score calculation completed.")   
    return df_cleaned, df_risk_score

#Step 3 Load

def load(df_cleaned, df_risk_score,engine):
    df_risk_score.to_sql("processed_agreements", engine,index=False, if_exists = "replace")
    logging.info("Processed data loaded successfully into the database.")
#Validation
    # df_check = pd.read_sql('SELECT * FROM processed_agreements', engine)
    # print(df_check)
    

#Excel Report Generation
def output(df_cleaned, df_risk_score):
    with pd.ExcelWriter("/workspaces/Danske-data-assignment/section2/report.xlsx") as writer:
        for asset, group in df_cleaned.groupby("asset_type"):
            group.to_excel(writer, sheet_name=asset, index=False)
    logging.info("Excel report created")
    summary = f"""
Total records processed: {len(df_cleaned)}
Date error records: {df_cleaned['has_date_error'].sum()}
Date logic error records: {df_cleaned['has_date_logic_error'].sum()}
Payment error records: {df_cleaned['has_payment_error'].sum()}
Total exposure (all customers): {df_risk_score['total_exposure'].sum()}
Average exposure (per customer): {df_risk_score['avg_exposure'].mean()}
"""
    with open("/workspaces/Danske-data-assignment/section2/report.txt", "w") as f:
        f.write(summary)
    logging.info("Summary report created")


def run_pipeline(engine):
    df_raw = extract(engine)
    df_cleaned, df_risk_score = transform(df_raw)
    load(df_cleaned, df_risk_score, engine)
    output(df_cleaned, df_risk_score)

run_pipeline(engine)
logging.info("Pipeline execution completed successfully. Processed data saved to database and report generated.")