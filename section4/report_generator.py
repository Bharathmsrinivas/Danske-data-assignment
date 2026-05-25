import pandas as pd
from jinja2 import Template

class ReportGenerator:

    def __init__(self, df: pd.DataFrame, template_path: str):
        self.df = df
        self.template_path = template_path

    def render_html(self, output_path: str, title: str = "Report") -> None:
        with open(self.template_path, "r") as f:
            template = Template(f.read())

        summary = self.df.describe().to_string()
        table = self.df.head(20).to_html(index=False)

        html_content = template.render(
        title=title,
        summary=summary,
        table=table
    )

        with open(output_path, "w") as f:
            f.write(html_content)


    def export_excel(self, output_path: str) -> None:
        self.df.to_excel(output_path, index=False)


    def export_txt(self, output_path: str) -> None:
        with open(output_path, "w") as f:
            f.write("===== Summary =====\n")
            f.write(self.df.describe().to_string())
            
            f.write("\n\n===== Data Preview =====\n")
            f.write(self.df.head(20).to_string())