import streamlit as st
import pandas as pd
import plotly.express as px

# Load the 'WWTP' sheet
file_path = 'IW-TEC-100-007.xlsx'
wwtp_df = pd.read_excel(file_path, sheet_name='WWTP')

# Drop fully empty rows and columns
wwtp_df.dropna(how='all', axis=1, inplace=True)
wwtp_df.dropna(how='all', axis=0, inplace=True)

# Inspect the structure
st.write("First few rows of the WWTP sheet:")
st.dataframe(wwtp_df.head(20))

# Define columns based on hierarchical levels observed (adjust as necessary)
columns = ['Level 5', 'Ref Level 5', 'Level 6', 'Ref Level 6', 'Level 7', 'Ref Level 7', 'Level 8', 'Ref Level 8', 'Level 9', 'Ref Level 9']
wwtp_df.columns = columns[:len(wwtp_df.columns)]

# Drop rows where Level 5 is NaN as these are not relevant to the hierarchy
hierarchy_data = wwtp_df.dropna(subset=['Level 5'])

# Fill forward to propagate level values down the hierarchy
hierarchy_data.fillna(method='ffill', inplace=True)

# Select relevant columns and ensure completeness
hierarchy_df = hierarchy_data[columns].dropna().reset_index(drop=True)

# Streamlit app
st.title('Wastewater Treatment Plant Hierarchy')

# Create a treemap using plotly
fig = px.treemap(
    hierarchy_df,
    path=['Level 5', 'Level 6', 'Level 7', 'Level 8', 'Level 9'],
    values=[1]*len(hierarchy_df),  # Assigning an arbitrary value for size
    color='Level 5',
    hover_data={'Ref Level 5': True, 'Ref Level 6': True, 'Ref Level 7': True, 'Ref Level 8': True, 'Ref Level 9': True}
)

# Display the treemap in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Display a table for detailed view
st.subheader("Detailed Hierarchy Data")
st.dataframe(hierarchy_df)
