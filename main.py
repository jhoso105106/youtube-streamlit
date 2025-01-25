import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.title("もくもく会アンケート")

# 画像ファイルのアップロード
uploaded_files = st.file_uploader("画像ファイルをアップロードしてください", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    images = [Image.open(uploaded_file) for uploaded_file in uploaded_files]
    for img, uploaded_file in zip(images, uploaded_files):
        st.image(img, caption=f"アップロードされた画像: {uploaded_file.name}", use_column_width=True)
        
    # テキスト入力
    #st.title("8.何かアイディア等あれば自由に書いてくださいをCopilotで集計しました")
    #text = st.write("8.何かアイディア等あれば自由に書いてくださいをCopilotで集計しました")

    st.title("8.何かアイディア等あれば自由に書いてくださいをCopilotで集計しました")

    st.markdown("""
    1. **事前アンケートの実施**
        - 参加者の選択コースや勉強中のステップ、当日のもくもく会で取り組む内容を把握する。
        - 事前アンケート結果を共有し、全員の状況を把握。
    
    2. **解決したい問題の事前募集**
        - 技術的な問題や解決したいことを事前に募集し、当日に向けて準備する。
        - 参加者同士でアイデアを共有し、解決に向けて協力する。
    
    3. **ポマドーロ効果の導入**
        - 25分間の集中作業と5分間の休憩を繰り返すリズムを設定。
        - 休憩時間に雑談や質問タイムを設ける。
    
    4. **ブレイクアウトルームの活用**
        - 大人数の場合、学習内容やレベルごとにルームを分ける。
        - ブレイクアウトルームでの作業中にテキストチャットやボイスチャットで質問や交流を行う。
    """)

    if text:
        for img in images:
            draw = ImageDraw.Draw(img)
            # フォントの設定 (デフォルトフォント)
            font = ImageFont.load_default()

            # テキストの位置を指定 (例: 左上に配置)
            position = (10, 10)

            # 画像にテキストを描画
            draw.text(position, text, fill="white", font=font)
        
        for img, uploaded_file in zip(images, uploaded_files):
            st.image(img, caption=f"テキストが追加された画像: {uploaded_file.name}", use_column_width=True)

