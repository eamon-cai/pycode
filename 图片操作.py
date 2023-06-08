from io import BytesIO
from PIL import Image

# 图片字节转换成image对象
img_byte = b"图片字节"
bytes_stream = BytesIO(img_byte)
image = Image.open(bytes_stream)

# image对象转换成图片字节
im = Image.open("code.jpg")
new_img = im.convert("RGB")
img_byte = BytesIO()
new_img.save(img_byte, format='PNG')  # format: PNG or JPEG
binary_content = img_byte.getvalue()  # im对象转为二进制流


