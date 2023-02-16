import streamlit as st
import pandas as pd
import os

# import common
default_pass = os.path.dirname(__file__)

# データ分析関連
df = pd.read_csv(default_pass + "\\平均気温.csv", index_col="月")
# st.dataframe(df)
# st.table(df)
st.line_chart(df)
st.bar_chart(df["2021年"])