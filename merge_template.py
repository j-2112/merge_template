import pandas as pd
import openpyxl
import os

desktop_location = os.path.join(os.environ['USERPROFILE'], 'Desktop')


# df1 = pd.read_excel(os.path.join(desktop_location, workbook_name), sheet_name=int(input("Left Sheet position: ")))
# df2 = pd.read_excel(os.path.join(desktop_location, workbook_name), sheet_name=int(input("Right Sheet position: ")))

# df3 = pd.merge(df1, df2, on=["year", "id"])


def merge_excel(wb_name, df1_sheet_position: int = 0, df2_sheet_position: int = 1, merge_on: list = None,
                sheet_out_name: str = "merged"):
    if merge_on is None:
        merge_on = ["id"]
    wb_name = wb_name.strip() + ".xlsx"
    df1 = pd.read_excel(os.path.join(desktop_location, wb_name), sheet_name=df1_sheet_position)
    df2 = pd.read_excel(os.path.join(desktop_location, wb_name), sheet_name=df2_sheet_position)
    df3 = pd.merge(df1, df2, on=merge_on)
    with pd.ExcelWriter(os.path.join(desktop_location, wb_name), mode="a", if_sheet_exists="replace") as writer:
        df3.to_excel(writer, sheet_name=sheet_out_name, index=False)


if __name__ == "__main__":
    merge_excel("merge", merge_on=["id", "year"])
