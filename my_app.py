import streamlit as st
import pandas as pd
import plotly.express as px

# Load and inspect the WWTP sheet
file_path = 'IW-TEC-100-007.xlsx'
wwtp_df = pd.read_excel(file_path, sheet_name='WWTP')

# Drop fully empty rows and columns
wwtp_df.dropna(how='all', axis=1, inplace=True)
wwtp_df.dropna(how='all', axis=0, inplace=True)

# Extract hierarchical levels
levels = wwtp_df['Return to Contents page'].dropna().unique()

# Creating a structured DataFrame based on observed patterns
data = []

# Loop through the DataFrame to create hierarchical data
for i, level in enumerate(levels):
    if "LEVEL 1" in level:
        level_1 = levels[i + 1]
    if "LEVEL 2" in level:
        level_2 = levels[i + 1]
    if "LEVEL 3" in level:
        level_3 = levels[i + 1]
    if "LEVEL 4" in level:
        level_4 = levels[i + 1]
    if "LEVEL 5" in level:
        level_5 = levels[i + 1]
        data.append([
            'Wastewater Treatment Plant',  # Adding the main plant type
            'WWTP',
            level_1, 'Ref1',
            level_2, 'Ref2',
            level_3, 'Ref3',
            level_4, 'Ref4',
            level_5, 'Ref5'
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
