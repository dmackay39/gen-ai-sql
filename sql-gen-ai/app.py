import db_utils as dbu
import gen_ai_model as gam
import streamlit as st

dbu.populate_table()
print(dbu.get_all_table_data())
print(dbu.execute_custom_query("""SELECT * FROM Movies WHERE rating=3"""))
st.sidebar.header("Natural Language Database Querying")
user_input = st.sidebar.text_input("Enter your natural language query here", value=None)
col1, col2 = st.columns(2)
with col1:
   st.header("Full table")
   st.write(dbu.get_all_table_data()) 
with col2:
   st.header("Query results")
   if user_input is not None:
      returned_query = gam.call_model(user_input)
      st.write(returned_query)
      st.write(dbu.execute_custom_query(f"""{returned_query}""")) 
   else:
      st.write("")