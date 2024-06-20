import streamlit as st
import pandas as pd
import csv


def create_csv_data(data):
  lines = data[table_name].strip().split('\n')
  # Extract headers and rows
  headers = [h.strip() for h in lines[0].split('|') if h.strip()]
  rows = [[col.strip() for col in line.split('|') if col.strip()] for line in lines[2:]]

  with open(f'{table_name}.csv', 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(headers)
      writer.writerows(rows)


#Run streamlit
# Sample data for demonstration
dummy_resp = {'claims_data': '| Claim_ID | Policyholder_ID | Adjuster_ID | Date_Filed | Date_Resolved | Claim_Type_ID | Amount     | Status_ID |\n|----------|-----------------|-------------|------------|---------------|---------------|------------|-----------|\n| 1001     | 1               | 1           | 2023-01-15 | 2023-06-15    | 1             | 10000.00   | 1         |\n| 1002     | 2               | 2           | 2023-06-20 | 2023-11-20    | 2             | 250000.50  | 2         |\n| 1003     | 3               | 3           | 2023-12-05 | 2023-12-25    | 3             | 500000.75  | 3         |\n| 1004     | 4               | 1           | 2023-02-10 | 2023-07-10    | 1             | 15000.00   | 4         |\n| 1005     | 5               | 2           | 2023-03-15 | 2023-08-15    | 2             | 300000.00  | 1         |\n| 1006     | 6               | 3           | 2023-04-20 | 2023-09-20    | 3             | 450000.25  | 2         |\n| 1007     | 7               | 1           | 2023-05-25 | 2023-10-25    | 1             | 20000.00   | 3         |\n| 1008     | 8               | 2           | 2023-06-30 | 2023-11-30    | 2             | 350000.75  | 4         |\n| 1009     | 9               | 3           | 2023-07-05 | 2023-12-05    | 3             | 50000.00   | 1         |\n| 1010     | 10              | 1           | 2023-08-10 | 2023-12-25    | 1             | 400000.50  | 2         |'}
table_name = list(dummy_resp.keys())[0]
create_csv_data(dummy_resp)

data = pd.read_csv(f"{table_name}.csv")

# Streamlit app layout
st.title("Table Viewer")

# Sidebar for table names
st.sidebar.title("Tables")
selected_table = None
for table_name in data.keys():
    if st.sidebar.button(table_name):
        selected_table = table_name

# Display the selected table data
if selected_table:
    st.header(f"Data for {selected_table}")
    st.dataframe(data[selected_table])
else:
    st.header("Please select a table from the sidebar")
