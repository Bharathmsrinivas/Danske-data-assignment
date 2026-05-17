import pandas as pd
from section1.cleaning import clean_agreements

def test_all_valid_data():
    df = pd.DataFrame({
        "agreement_id": ["A1"],
        "customer_id": ["C1"],
        "asset_type": ["CAR"],
        "start_date": ["2022-01-01"],
        "end_date": ["2023-01-01"],
        "monthly_payment": [100],
        "currency": ["eur"],
        "status": ["ACTIVE"]
    })
    # print(df_test1)
    result = clean_agreements(df)
    # print(result)
    assert result["has_date_error"].sum() == 0
    assert result["has_date_logic_error"].sum() == 0
    assert result["has_payment_error"].sum() == 0

def test_all_invalid_data():
    df = pd.DataFrame({
        "agreement_id": ["A1"],
        "customer_id": [None],
        "asset_type": ["CAR"],
        "start_date": ["bad-date"],
        "end_date": ["2022-01-01"],
        "monthly_payment": [-100],
        "currency": ["EUR"],
        "status": ["active"]
    })
    result = clean_agreements(df)
    assert result["has_date_error"].sum() == 1
    assert result["has_payment_error"].sum() == 1
    assert result["has_date_logic_error"].sum() == 0

def test_invalid_date():
    df = pd.DataFrame({
        "agreement_id": ["A1"],
        "customer_id": ["C1"],
        "asset_type": ["CAR"],
        "start_date": ["invalid-date"],
        "end_date": ["2023-01-01"],
        "monthly_payment": [100],
        "currency": ["EUR"],
        "status": ["active"]
    })
    # print(df)
    result = clean_agreements(df)
    # print(result)
    assert result["has_date_error"].sum() == 1

def test_date_logic_error():
    df = pd.DataFrame({
        "agreement_id": ["A1"],
        "customer_id": ["C1"],
        "asset_type": ["CAR"],
        "start_date": ["2023-01-01"],
        "end_date": ["2022-01-01"],
        "monthly_payment": [100],
        "currency": ["EUR"],
        "status": ["active"]
    })
    # print(df)
    result = clean_agreements(df)
    # print(result)
    assert result["has_date_logic_error"].sum() == 1

def test_payment_error():
    df = pd.DataFrame({
        "agreement_id": ["A1"],
        "customer_id": ["C1"],
        "asset_type": ["CAR"],
        "start_date": ["2022-01-01"],
        "end_date": ["2023-01-01"],
        "monthly_payment": [-100],
        "currency": ["EUR"],
        "status": ["active"]
    })
    # print(df)
    result = clean_agreements(df)
    # print(result)
    assert result["has_payment_error"].sum() == 1

# test_all_valid_data()
# test_invalid_date()
# test_date_logic_error()
# test_payment_error()