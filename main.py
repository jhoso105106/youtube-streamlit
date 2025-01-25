import streamlit as st
from PIL import Image
import os

# 保存するディレクトリを指定
save_dir = "uploaded_images"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

st.title("画像アップロードと保存アプリ")

# 画像ファイルのアップロード
uploaded_files = st.file_uploader("画像ファイルをアップロードしてください", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        # 画像を保存
        img = Image.open(uploaded_file)
        img.save(os.path.join(save_dir, uploaded_file.name))
        st.image(img, caption=f"アップロードされた画像: {uploaded_file.name}", use_column_width=True)
        st.success(f"画像が保存されました: {uploaded_file.name}")

# 保存ディレクトリにある画像を表示
st.title("保存された画像")
if os.listdir(save_dir):
    for file_name in os.listdir(save_dir):
        file_path = os.path.join(save_dir, file_name)
        img = Image.open(file_path)
        st.image(img, caption=f"保存された画像: {file_name}", use_column_width=True)
else:
    st.write("保存された画像はありません")

