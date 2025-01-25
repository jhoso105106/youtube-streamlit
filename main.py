import streamlit as st
from PIL import Image
import os

# 保存するディレクトリを指定
save_dir = "uploaded_images"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

st.title("もくもく会アンケート")

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
    text=st.title("8.何かアイディア等あれば自由に書いてくださいをCopilotで集計しました")

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
    
    5. **ウェルカムチャットの最適化**
        - 入室時のウェルカムチャットを工夫し、運営側が集中できる環境を整える。
        - 情報交換したい方と集中作業したい方を分ける。
    
    6. **共有サイトの作成**
        - 「Copilotにこんなプロンプトを入力したらこんな生成してくれたよ」といった生成結果を気軽に投稿できるサイトを作成。
        - もくもく会で遭遇したエラーや解決方法をドキュメントとして共有する。
    
    ### 実現可能な運営方法
    - **定期的なアナウンス**:
        - 毎週固定の曜日と時間でアナウンスを行い、参加者を集める。
    - **途中入退出自由**:
        - 参加者が自由に参加し、途中で退出できる環境を提供。
    - **成果の記録**:
        - 参加者が最初にやることを一覧表に記入し、時間終わりに成果を記入。
        - 最後に10分間の成果発表、情報交換、質疑の時間を設ける。
    - **ツールの活用**:
        - Slack、パドルミーティング、Canvasなどのツールを使用して情報共有や記録を行う。
    """)
    

