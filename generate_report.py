import pandas as pd
from fpdf import FPDF

# 1. Read Data
data = pd.read_csv('data.csv')

# 2. Analyze Data (basic summary stats)
summary = data.describe()

# 3. Generate PDF Report
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Data Analysis Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, label):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, label, 0, 1, 'L')
        self.ln(2)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 10, body)
        self.ln()

# Create PDF
pdf = PDF()
pdf.add_page()

pdf.chapter_title("Summary Statistics")
pdf.set_font("Arial", size=10)

# Add summary statistics table
col_width = pdf.w / (len(summary.columns) + 1)
row_height = 8

# Header
pdf.set_fill_color(200, 220, 255)
pdf.set_font('Arial', 'B', 10)
pdf.cell(col_width, row_height, 'Stat', border=1, fill=True)
for col in summary.columns:
    pdf.cell(col_width, row_height, str(col), border=1, fill=True)
pdf.ln(row_height)

# Rows
pdf.set_font('Arial', '', 10)
for idx, row in summary.iterrows():
    pdf.cell(col_width, row_height, str(idx), border=1)
    for val in row:
        pdf.cell(col_width, row_height, f"{val:.2f}", border=1)
    pdf.ln(row_height)

# Save PDF
pdf.output("report.pdf")

print("PDF report generated as report.pdf")