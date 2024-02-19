import re
import base64
from email.parser import Parser

def extract_images_from_mhtml(mhtml_path):
    # 读取MHTML文件
    with open(mhtml_path, 'r') as file:
        mhtml_content = file.read()

    # 解析MHTML内容
    email_message = Parser().parsestr(mhtml_content)

    # 初始化图片计数器
    image_counter = 1

    # 遍历MHTML中的所有部分
    for part in email_message.walk():
        # 检查内容类型是否为image
        if part.get_content_maintype() == 'image':
            # 获取图片内容和图片类型
            image_data = part.get_payload(decode=True)
            image_type = part.get_content_subtype()

            # 构建图片文件名
            image_filename = f'image_{image_counter}.{image_type}'

            # 保存图片
            with open(image_filename, 'wb') as img_file:
                img_file.write(image_data)
                print(f'Saved {image_filename}')

            # 更新图片计数器
            image_counter += 1

# 示例：从指定MHTML文件中提取图片
mhtml_path = '1.mhtml'
extract_images_from_mhtml(mhtml_path)
