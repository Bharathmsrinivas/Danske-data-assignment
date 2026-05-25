# Danske-data-assignment

This project processes asset finance data to build a structured ETL pipeline, generate risk-related insights, and produce reusable reporting outputs for analysis and business use.

## Setup

Install required libraries:
pip install -r requirements.txt

## Run

Run pipeline:
python -m section2.pipeline

Run tests:
pytest

## AI Usage

AI assistance was used to explore libraries such as Polars and pytest. All core logic, design decisions, and implementations were developed independently.

---

## Possible Improvements

While the current implementation provides a complete working solution, the following enhancements could make it more robust and production-ready:

### 1. Reliability & Error Handling
- Add proper exception handling for database connections, file operations, and transformations to ensure safe failure handling without crashing the pipeline.
- Improve error handling in the ETL pipeline so that failures in one step do not break the entire workflow.

### 2. Monitoring & Operational Readiness
- In a production environment, pipelines are usually scheduled (e.g., Airflow, cron jobs). Adding monitoring and alerting (email notifications or other mechanisms) would help track failures and ensure timely recovery.

### 3. Scalability & Performance
- For larger datasets, the solution can be extended to use distributed processing frameworks such as PySpark for better scalability.
- Performance can be further enhanced with optimized data storage and processing techniques such as Delta Lake and Parquet formats.
- For large and frequently updating datasets, **incremental data loading** can be used to process only **new or changed records** instead of reprocessing the entire dataset each time. This improves **performance** and supports **near real-time processing**.

### 4. Future Enhancements
The following areas were not fully implemented due to time constraints and are identified as future improvements:

- **Class-based pipeline design** to improve modularity and reusability
- Advanced **reporting framework enhancements**
- Improved **test coverage** including integration scenarios

---

## Project Details

This project uses asset finance data, where loan agreement records are processed to derive customer exposure and risk-related insights, supporting analysis of customer behaviour, payments, and portfolio risk.

---

## Dataset Overview

The dataset represents loan agreements in CSV format, where each record corresponds to a financial contract. It supports multiple analytical use cases such as:

- Exposure analysis  
- Customer behaviour analysis  
- Payment pattern analysis  
- Delinquency tracking  
- Portfolio monitoring  

As the data originates from operational systems, it contains quality issues that can impact downstream reporting and analytics. The pipeline addresses this by applying structured validation and processing to make the data reliable for business use.

---

## Pipeline Overview

The project implements a structured data processing pipeline following an ETL pattern:

Data Ingestion → Data Cleaning → Transformation → Loading → Reporting

### Key components:
- Data quality checks to standardize and validate raw data  
- Transformation layer to prepare analytics-ready datasets  
- Centralized storage in a SQLite database  
- Output generation for different stakeholders  

---

## Outputs

The processed data is delivered in multiple formats to support different use cases:

- Excel → contains the full dataset, allowing business users to perform analysis  
- Text output → provides a summary and preview for validation and monitoring  
- Database → supports analytics, data modeling, and reporting  

---

## SQL & Analytics Layer

SQL queries demonstrate how structured data can be used to answer key business scenarios, including:

- Identifying high-exposure customers  
- Analyzing payment behaviour patterns  
- Detecting inactivity and potential risk signals  

This layer reflects real analytical usage and can be extended with proper data modeling (e.g., star schema design) to support dashboards and reporting.

---

## Performance Comparison

Benchmark results were evaluated on both small and large datasets to understand scalability.

## Performance Comparison

Benchmark results were evaluated on both small and large datasets to understand scalability.

### Small dataset (~5,000 rows)

| Method                | Time (sec) |
|---------------------|------------|
| Original (iterrows) | ~0.23      |
| Pandas (vectorized) | ~0.005     |
| Polars              | ~0.09      |

### Large dataset (~5 million rows)

| Method                | Time (sec) |
|---------------------|------------|
| Original (iterrows) | ~178       |
| Pandas (vectorized) | ~0.58      |
| Polars              | ~0.91      |
### Summary

- Vectorized processing significantly outperforms row-wise execution  
- Pandas performs efficiently at this scale  
- Polars provides competitive performance and is well-suited for larger datasets  

---

## Reporting Framework

A reusable reporting component is implemented to generate outputs from processed data in multiple formats. It accepts a dataset along with a template and produces:

- HTML report → structured presentation using a template with summary and tabular data  
- Excel output → full dataset for business analysis  
- Text output → summary and data preview for validation and monitoring  

This approach allows the same data to be reused across reporting, analysis, and monitoring scenarios.

---

## Practical Usage

This pipeline can be executed periodically (daily/weekly/monthly) to process new incoming data. Each run updates the cleaned and transformed dataset and refreshes outputs.

This ensures analytics, metrics, and reporting outputs always reflect the latest data, supporting continuous monitoring of customer behaviour and portfolio risk.

---

## Conclusion

This project demonstrates an end-to-end data workflow from raw data processing to analytics-ready outputs and reporting, reflecting practical data engineering and reporting practices.
