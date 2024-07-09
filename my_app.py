import streamlit as st
import pandas as pd
import plotly.express as px

# Load the spreadsheet file uploaded by the user
file_path = 'Valid Hierarchy Values 07-05-2024.xlsx'

# Load the data from the file
sheets = pd.read_excel(file_path, sheet_name=None)

# Extract the sheet names to understand the structure
sheet_names = list(sheets.keys())

# Assume we are working with the first sheet for the hierarchy visualization
df = sheets[sheet_names[0]]

# For visualization purposes, let's assume the hierarchy is represented by the first few columns
# This needs to be adjusted based on the actual structure of the sheet

# Assuming columns represent levels in the hierarchy
hierarchy_columns = df.columns[:5]  # Adjust this based on actual data
hierarchy_df = df[hierarchy_columns]

# Fill NA values to ensure proper hierarchical display
hierarchy_df = hierarchy_df.fillna(method='ffill')

# Create a treemap visualization using plotly with enhanced colors and text wrapping
fig = px.treemap(
    hierarchy_df,
    path=hierarchy_columns,
    values=[1]*len(hierarchy_df),  # Arbitrary values to create the treemap
    color=hierarchy_columns[0],  # Coloring based on the top level
    color_discrete_sequence=px.colors.qualitative.Pastel
)

# Update layout for text wrapping
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),
    treemapcolorway=px.colors.qualitative.Pastel
)

# Apply text wrapping to the treemap
fig.data[0].textinfo = 'label+text'
fig.update_traces(texttemplate='%{label}<br>%{text}')

# Display the treemap in Streamlit
st.title('ADH')
st.plotly_chart(fig, use_container_width=True)
