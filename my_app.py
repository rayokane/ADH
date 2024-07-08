import streamlit as st
import pandas as pd
import plotly.express as px

# Load the 'WWTP' sheet
file_path = '/IW-TEC-100-007.xlsx'
wwtp_df = pd.read_excel(file_path, sheet_name='WWTP')

# Drop fully empty rows and columns
wwtp_df.dropna(how='all', axis=1, inplace=True)
wwtp_df.dropna(how='all', axis=0, inplace=True)

# Clean and prepare data
wwtp_df.columns = ['Hierarchy']
wwtp_df = wwtp_df.dropna().reset_index(drop=True)

# Find indices for each level
level_indices = wwtp_df[wwtp_df['Hierarchy'].str.contains('LEVEL')].index.tolist()
levels = ['Level 5', 'Level 6', 'Level 7', 'Level 8', 'Level 9']

# Creating a hierarchical data structure
data = []
current_hierarchy = [''] * len(levels)

for i in range(len(wwtp_df)):
    if i in level_indices:
        level = level_indices.index(i)
        continue
    current_hierarchy[level] = wwtp_df.loc[i, 'Hierarchy']
    if level == 4:
        data.append([
            'Wastewater Treatment Plant', 'WWTP',
            current_hierarchy[0], 'Ref5',
            current_hierarchy[1], 'Ref6',
            current_hierarchy[2], 'Ref7',
            current_hierarchy[3], 'Ref8',
            current_hierarchy[4], 'Ref9'
        ])

# Convert to DataFrame
hierarchy_df = pd.DataFrame(data, columns=[
    'Plant Type', 'Plant Type Ref', 'Level 5', 'Ref Level 5', 'Level 6', 'Ref Level 6', 'Level 7', 'Ref Level 7', 'Level 8', 'Ref Level 8', 'Level 9', 'Ref Level 9'
])

# Streamlit app
st.title('Wastewater Treatment Plant Hierarchy')

# Create a treemap using plotly
fig = px.treemap(
    hierarchy_df,
    path=['Plant Type', 'Level 5', 'Level 6', 'Level 7', 'Level 8', 'Level 9'],
    values=[1]*len(hierarchy_df),  # Assigning an arbitrary value for size
    color='Level 5',
    hover_data={'Plant Type Ref': True, 'Ref Level 5': True, 'Ref Level 6': True, 'Ref Level 7': True, 'Ref Level 8': True, 'Ref Level 9': True}
)

# Display the treemap in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Display a table for detailed view
st.subheader("Detailed Hierarchy Data")
st.dataframe(hierarchy_df)
