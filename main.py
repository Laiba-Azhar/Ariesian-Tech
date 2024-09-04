import pandas as pd
from ydata_profiling import ProfileReport

# Load the CSV data
df = pd.read_csv("sub-division_population_of_pakistan.csv")

# Create a profile report
profile = ProfileReport(df, title="Sub-Division Population of Pakistan")  # Set a descriptive title

# Save the report to an HTML file
profile.to_file("sub-division_population_of_pakistan_report.html")
