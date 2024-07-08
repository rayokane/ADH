import streamlit as st
import pandas as pd
import plotly.express as px

# Load the 'Contents' sheet and inspect rows following the 'Level 5' placeholder
file_path = 'IW-TEC-100-007.xlsx'
contents_df = pd.read_excel(file_path, sheet_name='Contents')

# Find the index of the 'Level 5' placeholder
level_5_index = contents_df[contents_df['Unnamed: 0'] == 'Level 5'].index[0]

# Extract rows following the 'Level 5' placeholder
level_5_items = contents_df.iloc[level_5_index + 3:level_5_index + 10]
level_5_items = level_5_items[['Unnamed: 0', 'Unnamed: 1']].dropna()
level_5_items.columns = ['Level 5', 'Reference']

# Streamlit app
st.title('Level 5 Items')
st.write('The following are the Level 5 items identified from the document:')
st.dataframe(level_5_items)

# Create a simple bar chart to visualize Level 5 items
fig = px.bar(level_5_items, x='Level 5', y='Reference', title='Level 5 Items and References')
st.plotly_chart(fig, use_container_width=True)
