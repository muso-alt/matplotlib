import pandas as pd
import pandas_profiling
import sweetviz as sv
from pandasgui import show

df = pd.read_csv("testData.csv")

profile = pandas_profiling.ProfileReport(df)
profile.to_file("pandas_profiling_report.html")

compare_report = sv.analyze(df)
compare_report.show_html("sweetviz_report.html")

gui = show(df)

gui.show()
