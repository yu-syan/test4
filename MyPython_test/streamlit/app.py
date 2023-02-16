import streamlit as st
from PIL import Image
import datetime
import pandas as pd
import matplotlib.pyplot as plt

DEFAULT_FOLD_NAME = "streamlit"

st.title("サプーアプリ")
st.caption("これはサプーの動画用のテストアプリです")

# st.columns(2)：(2)は何分割するかの指定
# col1：左半分を扱う変数
# col2：右半分を扱う変数
col1, col2 = st.columns(2)

with col1:

    st.subheader("自己紹介")
    st.text("Python勉強中です！")

    # WordPressでよくあるコードをそのまま載せられるような見た目
    code = '''
    import streamlit as st

    st.title("サプーアプリ")
    '''

    st.code(code, language="python")

    # 画像(web画面上の画像URLをそのまま設定してもOK)
    image = Image.open(DEFAULT_FOLD_NAME + "\\" + "Twitterアイコン.jpg")
    st.image(image, width=200)

    # # 動画(web画面上の動画URLをそのまま設定してもOK)ちょっと動作は重め
    # video_file = open("寿司打_Twitter用.mp4", "rb")
    # video_bytes = video_file.read()
    # st.video(video_bytes)

    # テキストボックス
    # 通常は値が入るタイミングは画面がリロードされたタイミング or テキストボックスからフォーカスが外れた時

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

with col2:
    
    # データ分析関連
    df = pd.read_csv(DEFAULT_FOLD_NAME + "\\" + "平均気温.csv", index_col="月")
    # st.dataframe(df)
    # st.table(df)
    st.line_chart(df)
    st.bar_chart(df["2021年"])

    # matplotlib
    flg, ax = plt.subplots()
    ax.plot(df.index, df["2021年"])
    ax.set_title("matplotlib graph")
    st.pyplot(flg)

