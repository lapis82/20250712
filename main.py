import streamlit as st
st.title('sj first webapp')
name=st.text_input ('name:')
menu=st.selectbox('favourite menu:', ['chocolate', 'lemonade', 'tea'])
if st.button('welcome'):
  st.write( 'Hello, ' +name+ '! your favourite menu is ' +menu+ '. it is fine!')
