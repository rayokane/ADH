import streamlit as st
import pandas as pd
import plotly.express as px

# Load the 'Contents' sheet
file_path = 'IW-TEC-100-007.xlsx'
contents_df = pd.read_excel(file_path, sheet_name='Contents')

# Find the index of the 'Level 5' placeholder
level_5_index = contents_df[contents_df['Unnamed: 0'] == 'Level 5'].index[0]

# Extract rows following the 'Level 5' placeholder
level_5_items = contents_df.iloc[level_5_index + 3:level_5_index + 10]
level_5_items = level_5_items[['Unnamed: 0', 'Unnamed: 1']].dropna()
level_5_items.columns = ['Level 5', 'Reference']

# Function to load level 6 data from each sheet
def load_level_6_data(sheet_name):
    sheet_df = pd.read_excel(file_path, sheet_name=sheet_name)
    sheet_df.dropna(how='all', axis=1, inplace=True)
    sheet_df.dropna(how='all', axis=0, inplace=True)
    return sheet_df

# Dictionary to map Level 5 to their corresponding sheets
sheet_mapping = {
    'Water Treatment Plant': 'WTP',
    'Water Network Pumping Station': 'WNPS',
    'Water Network Storage': 'WNS',
    'Water Abstraction Point': 'WAP',
    'Water Network Monitoring Point': 'WNMP',
    'Raw Water Pumping Station': 'RWPS'
}

# Collect Level 6 data
level_6_data = []

for level_5, sheet in sheet_mapping.items():
    sheet_df = load_level_6_data(sheet)
    for _, row in sheet_df.iterrows():
        level_6_data.append([level_5, row[0]])

# Convert to DataFrame
level_6_df = pd.DataFrame(level_6_data, columns=['Level 5', 'Level 6'])

# Merge Level 5 and Level 6 data
merged_df = pd.merge(level_5_items, level_6_df, on='Level 5')

# Streamlit app
st.title('Level 5 and Level 6 Items')
st.write('The following are the Level 5 and Level 6 items identified from the document:')
st.dataframe(merged_df)

# Create a treemap to visualize Level 5 and Level 6 items
fig = px.treemap(
    merged_df,
    path=['Level 5', 'Level 6'],
    values=[1]*len(merged_df),  # Assigning an arbitrary value for size
    color='Level 5',
    hover_data={'Reference': True}
)
st.plotly_chart(fig, use_container_width=True)
