import streamlit as st
import pandas as pd
import plotly.express as px

# Load the full WWTP hierarchy from the Excel file
file_path = '/mnt/data/IW-TEC-100-007.xlsx'
wwtp_df = pd.read_excel(file_path, sheet_name='WWTP')

# Clean the data by dropping any fully empty columns and rows
wwtp_df.dropna(how='all', axis=1, inplace=True)
wwtp_df.dropna(how='all', axis=0, inplace=True)

# Display the cleaned data to understand its structure
st.write("First few rows of the WWTP sheet:")
st.dataframe(wwtp_df.head())

# Assuming columns represent hierarchical levels, extract these into a structured DataFrame
# The columns to extract will depend on actual column names/structure seen in the above step
# Example below assumes a certain structure, adjust as necessary
columns_to_use = ['Return to Contents page', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']

# Renaming columns for clarity
wwtp_df.columns = ['Level 1', 'Ref Level 1', 'Level 2', 'Ref Level 2', 'Level 3', 'Ref Level 3', 'Level 4', 'Ref Level 4', 'Level 5', 'Ref Level 5']

# Filtering necessary columns
hierarchy_data = wwtp_df[['Level 1', 'Ref Level 1', 'Level 2', 'Ref Level 2', 'Level 3', 'Ref Level 3', 'Level 4', 'Ref Level 4', 'Level 5', 'Ref Level 5']].dropna()

# Creating a hierarchical data structure
data = []

for _, row in hierarchy_data.iterrows():
    data.append([
        'Wastewater Treatment Plant',  # Adding the main plant type
        'WWTP',
        row['Level 1'], row['Ref Level 1'],
        row['Level 2'], row['Ref Level 2'],
        row['Level 3'], row['Ref Level 3'],
        row['Level 4'], row['Ref Level 4'],
        row['Level 5'], row['Ref Level 5']
    ])

# Convert to DataFrame
hierarchy_df = pd.DataFrame(data, columns=[
    'Plant Type', 'Plant Type Ref', 'Level 1', 'Ref Level 1', 'Level 2', 'Ref Level 2', 'Level 3', 'Ref Level 3', 'Level 4', 'Ref Level 4', 'Level 5', 'Ref Level 5'
])

# Streamlit app
st.title('Wastewater Treatment Plant Hierarchy')

# Create a treemap using plotly
fig = px.treemap(
    hierarchy_df,
    path=['Plant Type', 'Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5'],
    values=[1]*len(hierarchy_df),  # Assigning an arbitrary value for size
    color='Level 1',
    hover_data={'Plant Type Ref': True, 'Ref Level 1': True, 'Ref Level 2': True, 'Ref Level 3': True, 'Ref Level 4': True, 'Ref Level 5': True}
)

# Display the treemap in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Display a table for detailed view
st.subheader("Detailed Hierarchy Data")
st.dataframe(hierarchy_df)
