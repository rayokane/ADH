import streamlit as st
import pandas as pd
import plotly.express as px

# Sample hierarchical data with more levels
data = [
    ['Water Treatment Plant', 'WTP', 'ACCESS CONTROL SECURITY', 'ACCS', 'ACCESS CONTROL', 'ACCC'],
    ['Water Treatment Plant', 'WTP', 'ACCESS CONTROL SECURITY', 'ACCS', 'CCTV', 'CCTV'],
    ['Water Treatment Plant', 'WTP', 'ACCESS CONTROL SECURITY', 'ACCS', 'GATE | BARRIER', 'GOB'],
    ['Water Network Pumping Station', 'WNPS', 'ACTUATOR', 'ACTU', 'ELECTRIC', 'ELEC'],
    ['Water Network Pumping Station', 'WNPS', 'ACTUATOR', 'ACTU', 'HYDRAULIC', 'HLIC'],
    ['Water Network Pumping Station', 'WNPS', 'ACTUATOR', 'ACTU', 'MANUAL', 'MANU'],
    ['Water Network Pumping Station', 'WNPS', 'ACTUATOR', 'ACTU', 'PNEUMATIC', 'PNEU'],
    ['Water Network Storage', 'WNS', 'AERATOR', 'ARTR', 'CASCADE', 'CASC'],
    ['Water Network Storage', 'WNS', 'AERATOR', 'ARTR', 'DIFFUSED - COARSE', 'DIFC'],
    ['Water Network Storage', 'WNS', 'AERATOR', 'ARTR', 'DIFFUSED - FINE', 'DIFI'],
    ['Water Network Storage', 'WNS', 'AERATOR', 'ARTR', 'MECHANICAL - SURFACE', 'MSUR'],
    ['Water Abstraction Point', 'WAP', 'AIR CONDITIONING', 'ACON', 'HEVAC', 'HEVA'],
    ['Water Abstraction Point', 'WAP', 'AIR CONDITIONING', 'ACON', 'PROCESS', 'PROC'],
    ['Waste Water Treatment Plant', 'WWTP', 'AIR TREATMENT', 'AIRT', 'BIO MEDIA', 'BMED'],
    ['Waste Water Treatment Plant', 'WWTP', 'AIR TREATMENT', 'AIRT', 'CARBON', 'CARB'],
    ['Waste Water Treatment Plant', 'WWTP', 'AIR TREATMENT', 'AIRT', 'CHEMICAL (SCRUBBER)', 'CHES'],
    ['Waste Water Treatment Plant', 'WWTP', 'AIR TREATMENT', 'AIRT', 'DUST', 'DUST'],
    ['Waste Water Treatment Plant', 'WWTP', 'AIR TREATMENT', 'AIRT', 'LIQUID PHASE (SEPTICITY)', 'LPHA'],
    ['Waste Water Treatment Plant', 'WWTP', 'AIR TREATMENT', 'AIRT', 'PACKAGE', 'PACK']
]

# Convert to DataFrame
hierarchy_df = pd.DataFrame(data, columns=[
    'Plant Type', 'Plant Type Ref', 'Level 8 Class 1', 'L8 Ref Class 1', 'Level 8 Class 2', 'L8 Ref Class 2'
])

# Streamlit app
st.title('Asset Hierarchy')

# Create a treemap using plotly
fig = px.treemap(
    hierarchy_df,
    path=['Plant Type', 'Level 8 Class 1', 'Level 8 Class 2'],
    values=[1]*len(hierarchy_df),  # Assigning an arbitrary value for size
    color='Plant Type',
    hover_data={'Plant Type Ref': True, 'L8 Ref Class 1': True, 'L8 Ref Class 2': True}
)

# Display the treemap in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Display a table for detailed view
st.subheader("Detailed Hierarchy Data")
st.dataframe(hierarchy_df)
