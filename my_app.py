import streamlit as st
import pandas as pd
import plotly.express as px

# Load the hierarchical data (using the same sample data as before)
data = [
    ['ACCESS CONTROL SECURITY', 'ACCS', 'ACCESS CONTROL', 'ACCC'],
    ['ACCESS CONTROL SECURITY', 'ACCS', 'CCTV', 'CCTV'],
    ['ACCESS CONTROL SECURITY', 'ACCS', 'GATE | BARRIER', 'GOB'],
    ['ACTUATOR', 'ACTU', 'ELECTRIC', 'ELEC'],
    ['ACTUATOR', 'ACTU', 'HYDRAULIC', 'HLIC'],
    ['ACTUATOR', 'ACTU', 'MANUAL', 'MANU'],
    ['ACTUATOR', 'ACTU', 'PNEUMATIC', 'PNEU'],
    ['AERATOR', 'ARTR', 'CASCADE', 'CASC'],
    ['AERATOR', 'ARTR', 'DIFFUSED - COARSE', 'DIFC'],
    ['AERATOR', 'ARTR', 'DIFFUSED - FINE', 'DIFI'],
    ['AERATOR', 'ARTR', 'MECHANICAL - SURFACE', 'MSUR'],
    ['AIR CONDITIONING', 'ACON', 'HEVAC', 'HEVA'],
    ['AIR CONDITIONING', 'ACON', 'PROCESS', 'PROC'],
    ['AIR TREATMENT', 'AIRT', 'BIO MEDIA', 'BMED'],
    ['AIR TREATMENT', 'AIRT', 'CARBON', 'CARB'],
    ['AIR TREATMENT', 'AIRT', 'CHEMICAL (SCRUBBER)', 'CHES'],
    ['AIR TREATMENT', 'AIRT', 'DUST', 'DUST'],
    ['AIR TREATMENT', 'AIRT', 'LIQUID PHASE (SEPTICITY)', 'LPHA'],
    ['AIR TREATMENT', 'AIRT', 'PACKAGE', 'PACK']
]

hierarchy_df = pd.DataFrame(data, columns=['Level 8 Class 1', 'L8 Ref Class 1', 'Level 8 Class 2', 'L8 Ref Class 2'])

# Streamlit app
st.title('Asset Hierarchy')

# Create a treemap using plotly
fig = px.treemap(
    hierarchy_df,
    path=['Level 8 Class 1', 'Level 8 Class 2'],
    values=[1]*len(hierarchy_df),  # Assigning an arbitrary value for size
    color='Level 8 Class 1',
    hover_data={'L8 Ref Class 1': True, 'L8 Ref Class 2': True}
)

# Display the treemap in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Display a table for detailed view
st.subheader("Detailed Hierarchy Data")
st.dataframe(hierarchy_df)
