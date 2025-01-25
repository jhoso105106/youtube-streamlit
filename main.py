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
    text = st.text_input("8何かアイディア等あれば自由に書いてくださいをCopilotで集計しました")

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

