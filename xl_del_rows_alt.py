import os
import pandas as pd
import numpy as np

desktop_location = os.path.join(os.environ['USERPROFILE'], 'Desktop')

xl_file_name = "test_rows.xlsx"
full_path = os.path.join(desktop_location, xl_file_name)
df = pd.read_excel(full_path)

series1 = df["name"]
series2 = df.iloc[:, 0]

print(series1)
print(series2)


df = np.array()
