import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(
    page_title="EcoLogix ESG & Carbon Compliance Dashboard",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Streamlit
st.markdown("""
<style>
    .main {
        background-color: #0f172a;
        color: #f8fafc;
    }
    .stMetric {
        background-color: #1e293b;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #334155;
    }
    .stSelectbox, .stTextInput {
        color: #f8fafc;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.image("https://img.icons8.com/isometric-line/100/111827/leaf.png", width=50)
st.sidebar.title("EcoLogix ESG")
st.sidebar.caption("ESG & Carbon Footprint Dashboard")

menu = st.sidebar.radio("Navigation", ["Overview & Analytics", "Fleet Telematics", "Audit Report Generator", "Settings"])

# Mock Data
emissions_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Scope 1 (Fleet)': [420, 390, 410, 370, 340, 310],
    'Scope 2 (Facilities)': [150, 145, 140, 130, 125, 110],
    'Scope 3 (Supply Chain)': [210, 195, 200, 180, 175, 160],
    'Target Limit': [800, 780, 760, 740, 720, 700]
})

fleet_df = pd.DataFrame([
    {'Vehicle ID': 'FL-104', 'Type': 'EV Freight', 'Model': 'Volvo FL Electric', 'Route': 'Urban Local', 'Emissions (kg/km)': 0.00, 'Efficiency': '98%', 'Status': 'Active'},
    {'Vehicle ID': 'FL-209', 'Type': 'Diesel Hauler', 'Model': 'Scania R500', 'Route': 'Interstate North', 'Emissions (kg/km)': 0.82, 'Efficiency': '74%', 'Status': 'Maintenance Due'},
    {'Vehicle ID': 'FL-312', 'Type': 'CNG Transporter', 'Model': 'Iveco S-Way', 'Route': 'Regional Cross', 'Emissions (kg/km)': 0.41, 'Efficiency': '89%', 'Status': 'Active'},
    {'Vehicle ID': 'FL-405', 'Type': 'Hybrid Rigid', 'Model': 'MAN TGM', 'Route': 'Suburban Loop', 'Emissions (kg/km)': 0.35, 'Efficiency': '91%', 'Status': 'Active'},
    {'Vehicle ID': 'FL-518', 'Type': 'Diesel Hauler', 'Model': 'Volvo FH16', 'Route': 'Interstate South', 'Emissions (kg/km)': 0.89, 'Efficiency': '68%', 'Status': 'High Emission Alert'}
])

if menu == "Overview & Analytics":
    st.title("🌱 ESG Compliance & Carbon Analytics")
    st.caption("Real-time fleet carbon accounting and GHG reporting metrics.")
    st.divider()

    # KPI Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Gross Emissions", value="630 MT CO₂e", delta="-8.4% vs last mo")
    with col2:
        st.metric(label="Scope 1 (Direct Fleet)", value="310 MT CO₂e", delta="-4.2% fuel burn")
    with col3:
        st.metric(label="Scope 2 & 3 Combined", value="270 MT CO₂e", delta="+1.1% power use", delta_color="inverse")
    with col4:
        st.metric(label="Fleet Electrification", value="34%", delta="Target: 50%")

    st.divider()

    # Charts Section
    col_chart, col_score = st.columns([2, 1])

    with col_chart:
        st.subheader("Emissions Trend by Scope (GHG Protocol)")
        st.bar_chart(emissions_data.set_index('Month')[['Scope 1 (Fleet)', 'Scope 2 (Facilities)', 'Scope 3 (Supply Chain)']])

    with col_score:
        st.subheader("ESG Rating")
        st.markdown("### Score: **A+**")
        st.progress(0.92, text="ISO 14064 Compliance: 92%")
        st.write("✔️ **Fleet Efficiency Standard:** 92/100")
        st.write("⚠️ **Biofuel Transition Rate:** 68/100")
        st.write("✔️ **Data Audit Readiness:** 98/100")

elif menu == "Fleet Telematics":
    st.title("🚛 Fleet Telematics & Vehicle Intensity")
    
    col_search, col_filter = st.columns([2, 1])
    with col_search:
        search_query = st.text_input("Search Vehicle ID or Model", "")
    with col_filter:
        vehicle_type = st.selectbox("Filter Vehicle Type", ["All", "EV Freight", "Diesel Hauler", "CNG Transporter", "Hybrid Rigid"])

    filtered_df = fleet_df.copy()
    if search_query:
        filtered_df = filtered_df[filtered_df['Model'].str.contains(search_query, case=False) | filtered_df['Vehicle ID'].str.contains(search_query, case=False)]
    if vehicle_type != "All":
        filtered_df = filtered_df[filtered_df['Type'] == vehicle_type]

    st.dataframe(filtered_df, use_container_width=True)

elif menu == "Audit Report Generator":
    st.title("📄 Audit Report Generator")
    st.write("Compile real-time telematics into official GHG Protocol & ISO 14064 reporting formats.")
    
    framework = st.selectbox("Select Reporting Standard", ["GHG Protocol Corporate Standard", "ISO 14064 Standard Framework", "EU CSRD Compliance"])
    format_type = st.radio("Export Format", ["PDF Document", "CSV Dataset", "JSON Telematics"])
    
    if st.button("Generate & Download Audit Report"):
        with st.spinner("Processing carbon accounting calculations..."):
            time.sleep(1.5)
        st.success(f"Report compiled successfully for {framework}!")
        st.download_button("Download Generated Report", data=fleet_df.to_csv(), file_name="esg_audit_report.csv", mime="text/csv")

elif menu == "Settings":
    st.title("⚙️ Dashboard Settings")
    st.text_input("Organization Name", "EcoLogix Logistics Corp")
    st.number_input("Target Net-Zero Target Year", value=2035)
    st.checkbox("Enable Automated High-Emission Alerts", value=True)
    st.button("Save Configuration")
