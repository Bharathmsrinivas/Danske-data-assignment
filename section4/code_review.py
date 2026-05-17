import pandas as pd
import sqlalchemy

# ISSUE: Hardcoded database credentials (security risk)
# Password should not be stored in code; should use environment variables or secrets manager or OKTA or RSA
engine = sqlalchemy.create_engine("postgresql://admin:password123@prod-db:5432/finance")

def get_customer_data(customer_id):
    # User input should not be directly concatenated into SQL query
    query = "SELECT * FROM customers WHERE customer_id = '" + customer_id + "'"

    df = pd.read_sql(query, engine)

    data = []

    # ISSUE: Inefficient row-by-row processing (performance issue)
    
    for i in range(0, len(df)):
        row = df.iloc[i]

        data.append({
            'id': row['customer_id'],
            'name': row['customer_name'],
            'balance': float(row['balance'])
        })

    return data


def process_all_customers():
    all_ids = pd.read_sql("SELECT customer_id FROM customers", engine)

    results = []


    for id in all_ids['customer_id']:
        results.append(get_customer_data(id))


    return results

    