# ========================
# MYH dashboard
# ========================

# --- set up ---
import streamlit as st
from read_data import read_data # from a module, import a function
from kpis import approved_precentage, number_approved, total_applications

# --- reading data ---
df = read_data()

# --- dashboard components ---
#title
st.markdown("# YH dashboard 2024 application")

#description 
st.markdown("This is a simple dashboard about higher vocational education in Sweden (yrkeshögskola). The results from the education can be filtered in this dashboard.")

#kpi components (horizontally)
st.markdown("## KPIs in Sweden")

labels = ("Total applications", "Number of approved", "Approved percentage")
kpis = (total_applications, number_approved, approved_precentage)
cols = st.columns(3)

for col, label, kpi in zip(cols, labels, kpis):
    with col:
        st.metric(label=label, value=kpi)

#data table
st.markdown("## Raw data")
st.dataframe(df)

