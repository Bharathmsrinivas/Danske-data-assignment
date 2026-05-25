import pandas as pd
from section4.report_generator import ReportGenerator

df = pd.DataFrame({
    "customer": ["A", "B", "C"],
    "payment": [100, 200, 300]
})

report = ReportGenerator(df, "section4/template.html")
report.render_html("Sample_Report.html", title="Sample Report")
report.export_excel("Sample_Report.xlsx")
report.export_txt("Sample_Report.txt")