import streamlit as st
import pandas as pd
import plotly.express as px

# Load the spreadsheet file uploaded by the user
file_path = 'Valid Hierarchy Values 07-05-2024.xlsx'

# Load the data from the file
sheets = pd.read_excel(file_path, sheet_name=None)

# Extract the sheet names to understand the structure
sheet_names = list(sheets.keys())

# Function to load and display the first few rows of each sheet
def load_and_display_sheets(sheets):
    sheet_data = {}
    for sheet in sheet_names:
        sheet_df = sheets[sheet]
        sheet_data[sheet] = sheet_df.head()
    return sheet_data

# Load and display the sheets
sheet_data = load_and_display_sheets(sheets)

# Display the sheet names and the first few rows of each sheet
st.write("Sheet Names:", sheet_names)
for sheet, data in sheet_data.items():
    st.write(f"First few rows of {sheet} sheet:")
    st.dataframe(data)

# Assume we are working with the first sheet for the hierarchy visualization
df = sheets[sheet_names[0]]

# Display the first few rows of the selected sheet
st.write(f"First few rows of {sheet_names[0]} sheet:")
st.dataframe(df.head())

# For visualization purposes, let's assume the hierarchy is represented by the first few columns
# This needs to be adjusted based on the actual structure of the sheet

# Assuming columns represent levels in the hierarchy
hierarchy_columns = df.columns[:5]  # Adjust this based on actual data
hierarchy_df = df[hierarchy_columns]

# Fill NA values to ensure proper hierarchical display
hierarchy_df = hierarchy_df.fillna(method='ffill')

# Create a treemap visualization using plotly
fig = px.treemap(
    hierarchy_df,
    path=hierarchy_columns,
    values=[1]*len(hierarchy_df),  # Arbitrary values to create the treemap
    color=hierarchy_columns[0]  # Coloring based on the top level
)

# Display the treemap in Streamlit
st.title('Hierarchy Visualization')
st.plotly_chart(fig, use_container_width=True)
