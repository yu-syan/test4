import streamlit as st
# from PIL import Image
import datetime
# import pandas as pd
# import matplotlib.pyplot as plt

# 通常は↑タイミングで随時画面更新されるが、
# 枠線で囲まれて、ボタンを押すまではリロードしない。と設定(with st.form)
# ※keyは画面上に見える訳ではないので、認識し易いものでOK
with st.form(key="profile_form"):
    

    name = st.text_input("名前")
    address = st.text_input("住所")
    
    # # セレクトボックス
    # # 第一引数：フィールド名
    # # 第二引数：選択肢の内容
    # age_category = st.selectbox(
        
    #     "年齢層",
    #     ("子供(18才未満)", "大人(18才以上)")
                
    # )
    
    # ラジオボタン
    # 第一引数：フィールド名
    # 第二引数：選択肢の内容
    age_category = st.radio(
        
        "年齢層",
        ("子供(18才未満)", "大人(18才以上)")
                
    )
    
    # 複数選択
    # 第一引数：フィールド名
    # 第二引数：選択肢の内容
    hobby = st.multiselect(
        
        "趣味",
        ("スポーツ", "読書", "プログラミング", "アニメ・映画", "釣り", "料理")
                
    )
    
    # checkボックス
    maii_subscribe = st.checkbox("メールマガジンを購読する")
    
    # スライダー
    height = st.slider("身長", min_value=110, max_value=210)
    
    # 今日の日付
    dt_now = datetime.datetime.now()
    
    
    # 日付    
    start_date = st.date_input(
        "開始日",
        datetime.date(dt_now.year, dt_now.month, dt_now.day)
    )
    
    # カラーピッカー
    color = st.color_picker("テーマカラー", "#00f900")

    # ボタン(※引数はボタンの表示名)
    # 返却値：
    # ボタンが押されている：True
    # ボタンが押されていない：False
    submit_btn = st.form_submit_button("送信")
    cancel_bot = st.form_submit_button("キャンセル")

    if submit_btn:
        st.text(f'ようこそ！{name}さん！{address}に書類を送信しました！')
        st.text(f"年齢層：{age_category}")
        st.text(f"趣味；{','.join(hobby)}")



