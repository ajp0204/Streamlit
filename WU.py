import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import re 
st.set_page_config(page_title="WU Directory", layout="wide")
st.title('Directory at Westminster University')
st.write("This is an enhanced alternative to the employee [directory](https://westminsteru.edu/campus-directory/index.html) at Westminster University." )
data = pd.read_csv('WU_directory.csv')

#department selectbox
department_list = sorted(data['Department'].dropna().unique())
department_list.insert(0, 'All Departments')
col1, col2, col3  = st.columns([0.1,0.3,0.2])
with col1:
    st.text("Department:") 
with col2:
    department = st.selectbox(label = 'Choose one department from below:', options = department_list)
if department != 'All Departments':
    data = data.query("Department == @department")

#checkbox for role 
#role_faculty = st.checkbox('Faculty', value=1)
#role_staff = st.checkbox('Staff', value=1)
# col4 is empty 
col1, col2, col3, col4 = st.columns([0.2,0.2,0.2,0.4])
with col1:
    st.text("Type of Role:") 
with col2:
    role_faculty = st.checkbox('Faculty', value=1)
with col3:
    role_staff = st.checkbox('Staff', value=1)

if not role_faculty:
    data = data.query("Role == 'Staff'")
if not role_staff:
    data = data.query("Role == 'Faculty'")

#checkbox for contract
col1, col2, col3, col4 = st.columns([0.2,0.2,0.2,0.4])
with col1:
    st.text("Type of contract:") 
with col2:
    contract_full = st.checkbox('Full  Time', value=1)
with col3:
    contract_part = st.checkbox('Part Time', value=1)

if not contract_full:
    data = data.query("Contract == 'PART-TIME'")
if not contract_part:
    data = data.query("Contract == 'FULL-TIME'")

#checkbox for rank
col1, col2, col3, col4, col5 = st.columns([0.2,0.2,0.2,0.2, 0.4])
with col1:
    st.text("Rank of Faculty:") 
with col2:
    rank_assist = st.checkbox('Assistant', value=1)
with col3:
    rank_associate = st.checkbox('Associate', value=1)
with col4:
    rank_full = st.checkbox('Full', value=1)

if not rank_assist:
    data = data.query("Position != 'Assistant Professor'")
if not rank_associate:
    data = data.query("Position != 'Associate Professor'")
if not rank_full:
    data = data.query("Position == 'Assistant Professor' or Position == 'Associate Professor'", engine='python')    

#textbox for naming 
col1, col2, col3  = st.columns([0.1,0.2,0.2])
with col1:
    st.text("Name:") 
with col2:
    name = st.text_input(label = 'Type a condition:')
with col3:
    use_regex = st.checkbox("Regular Expression")

if name:
    data = data[data['Name'].str.contains(name, case=False, na=False, regex=use_regex)]


st.dataframe(data, hide_index=True)
