from PIL import Image

# 画像ファイルのパスを指定
image_path = '1.png'

# 画像を開く
image = Image.open(image_path)

# 画像を表示
image.show()
