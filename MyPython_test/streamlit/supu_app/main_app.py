import streamlit as st
from PIL import Image
# import common 
import os

# # 最初に参照先を強制的に1個下の回想にする
# try:
#     os.chdir('./streamlit')
# # エラーキャッチ後
# except Exception as e:
#     pass

default_pass = os.path.dirname(__file__)

st.title("サプーアプリ")
st.caption("これはサプーのテストアプリです")

# 画像(web画面上の画像URLをそのまま設定してもOK)
image = Image.open(default_pass + "\\Twitterアイコン.jpg")
st.image(image, width=200)