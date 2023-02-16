import streamlit as st

# WordPressでよくあるコードをそのまま載せられるような見た目
code = '''
import streamlit as st

st.title("サプーアプリ")
'''

st.code(code, language="python")