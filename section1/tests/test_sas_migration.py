import pandas as pd
from section1.sas_migration import calculate_risk_score


def test_risk_score_normal_case():
    df = pd.DataFrame({
        "customer_id": ["C1", "C1", "C2"],
        "monthly_payment": [100, 200, 300],
        "status": ["active", "closed", "active"]
    })
    result = calculate_risk_score(df)
    c1 = result[result["customer_id"] == "C1"]

    assert c1["total_exposure"].iloc[0] == 100
    assert c1["agreement_count"].iloc[0] == 1
    assert c1["avg_exposure"].iloc[0] == 100
    c2 = result[result["customer_id"] == "C2"]
    assert c2["total_exposure"].iloc[0] == 300
    assert c2["agreement_count"].iloc[0] == 1
    assert c2["avg_exposure"].iloc[0] == 300

def test_risk_score_no_active():
    df = pd.DataFrame({
        "customer_id": ["C1", "C1"],
        "monthly_payment": [100, 200],
        "status": ["active", "active"]
    })
    result = calculate_risk_score(df)
    c1 = result[result["customer_id"] == "C1"]

    assert c1["total_exposure"].iloc[0] == 300
    assert c1["agreement_count"].iloc[0] == 2
    assert c1["avg_exposure"].iloc[0] == 150

def test_risk_score_mixed():
    df = pd.DataFrame({
        "customer_id": ["C1", "C1"],
        "monthly_payment": [100, 200],
        "status": ["active", "closed"]
    })

    result = calculate_risk_score(df)

    c1 = result[result["customer_id"] == "C1"]

    assert c1["total_exposure"].iloc[0] == 100
    assert c1["agreement_count"].iloc[0] == 1
    assert c1["avg_exposure"].iloc[0] == 100