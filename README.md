# Danske-data-assignment


This project cleans loan agreement data, calculates risk scores, and builds a simple data pipeline.


Install required libraries: pip install -r requirements.txt

Execute : python -m section2.pipeline

Run Tests: Pytest

AI Usage : Some of the code snippets and to get myself familiarize with Polars, Pytest etc AI has been leveraged

**Possible Improvements**

While the current implementation provides a complete working solution, the following enhancements could make it more robust and production-ready:

**1. Reliability & Error Handling**
- Add proper exception handling for database connections, file operations, and transformations to ensure safe failure handling without crashing the pipeline.
- Improve error handling in the ETL pipeline so that failures in one step do not break the entire workflow.

**2. Monitoring & Operational Readiness**
- In a production environment, pipelines are usually scheduled (e.g., Airflow, cron jobs). Adding monitoring and alerting (email notifications or other way) would help track failures and ensure timely recovery.

**3. Scalability & Performance**
- For larger datasets, the solution can be extended to use distributed processing frameworks such as PySpark for better scalability.
- Performance can be further enhanced with optimized data storage and processing techniques like delta lake and parquet format.

The below Requirements are not implemented considering I have limited exposure and I would like to familiarise it before implementing.

**1. Class**
- A class-based design (e.g., encapsulating pipeline steps into a reusable class) could improve modularity and reusability.
- This is an area I am currently learning and planning to incorporate in future improvements.

**2. Reporting Framework (Section 4.2)**
- Due to time constraints and limited prior experience with Jinja2 templating, this section was not fully implemented.
- However, I plan to explore and implement this feature further to create reusable and extensible reporting components.

**3. Testing Enhancements**
- Increase unit test coverage to include more edge cases and integration-level testing.
- Add validation for pipeline-level execution and failure scenarios.

