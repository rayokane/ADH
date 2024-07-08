import streamlit as st
import pandas as pd

# Load the hierarchical data (replace 'path_to_hierarchy.csv' with your actual file path)
# For the sake of demonstration, we'll recreate the hierarchy dataframe from previous steps.
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

# Display the hierarchy in an expandable format
current_class = None

for index, row in hierarchy_df.iterrows():
    if row['Level 8 Class 1'] != current_class:
        if current_class is not None:
            st.markdown("---")
        current_class = row['Level 8 Class 1']
        st.subheader(f"{current_class} ({row['L8 Ref Class 1']})")
    st.write(f"&emsp; - {row['Level 8 Class 2']} ({row['L8 Ref Class 2']})")

