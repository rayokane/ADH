import streamlit as st
import pandas as pd
import plotly.express as px

# Load the 'WTP' sheet
file_path = 'IW-TEC-100-007.xlsx'
wtp_df = pd.read_excel(file_path, sheet_name='WTP')

# Drop fully empty rows and columns
wtp_df.dropna(how='all', axis=1, inplace=True)
wtp_df.dropna(how='all', axis=0, inplace=True)

# Inspect the structure
st.write("First few rows of the WTP sheet:")
st.dataframe(wtp_df.head(20))

# Define columns based on hierarchical levels observed (adjust as necessary)
columns = ['Level 1', 'Ref Level 1', 'Level 2', 'Ref Level 2', 'Level 3', 'Ref Level 3', 'Level 4', 'Ref Level 4', 'Level 5', 'Ref Level 5']
wtp_df.columns = columns[:len(wtp_df.columns)]

# Drop rows where Level 1 is NaN as these are not relevant to the hierarchy
hierarchy_data = wtp_df.dropna(subset=['Level 1'])

# Fill forward to propagate level values down the hierarchy
hierarchy_data.fillna(method='ffill', inplace=True)

# Select relevant columns and ensure completeness
hierarchy_df = hierarchy_data[columns].dropna().reset_index(drop=True)

# Streamlit app
st.title('Water Treatment Plant Hierarchy')

# Create a treemap using plotly
fig = px.treemap(
    hierarchy_df,
    path=['Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5'],
    values=[1]*len(hierarchy_df),  # Assigning an arbitrary value for size
    color='Level 1',
    hover_data={'Ref Level 1': True, 'Ref Level 2': True, 'Ref Level 3': True, 'Ref Level 4': True, 'Ref Level 5': True}
)

# Display the treemap in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Display a table for detailed view
st.subheader("Detailed Hierarchy Data")
st.dataframe(hierarchy_df)
