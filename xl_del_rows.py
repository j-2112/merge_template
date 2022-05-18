import os
import pandas as pd

desktop_location = os.path.join(os.environ['USERPROFILE'], 'Desktop')

xl_file_name = "test_rows.xlsx"
full_path = os.path.join(desktop_location, xl_file_name)
df = pd.read_excel(full_path)

# all_row_index = df.index
print(df.index)
row_header_list = []
for i in df.index:
    if "ca" in str(i):
        row_header_list.append(i)

row_header_list = list(set(row_header_list))

df = df.drop(labels=row_header_list, level=1)
print(df)
