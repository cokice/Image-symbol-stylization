
from PIL import Image, ImageDraw, ImageFont

def convert_image_to_textual_symbols(input_path, output_path):
    # 定义用于ASCII艺术的文本符号
    TEXTUAL_SYMBOLS = ["@", "#", "$", "%", "&", "*", "+", "-", ";", "."]
    # 请替换为您的字体文件路径
    
    
    # 打开图像文件
    image = Image.open(input_path)

    # 调整图像大小
    width, height = image.size
    aspect_ratio = height / float(width)
    new_width = 100  # 固定宽度
    new_height = int(aspect_ratio * new_width)
    image = image.resize((new_width, new_height))

    # 将图像转换为灰度
    image = image.convert('L')

    # 将灰度转换为文本符号
    pixels = list(image.getdata())
    textual_symbol_str = ""
    for pixel_value in pixels:
        textual_symbol_str += TEXTUAL_SYMBOLS[pixel_value * len(TEXTUAL_SYMBOLS) // 256]

    # 格式化符号字符串为图像形状
    textual_symbol_img_list = [textual_symbol_str[index:index + new_width] for index in range(0, len(textual_symbol_str), new_width)]

    # 调整字体高度以保持原始图像的纵横比
    font_width = 10  # 选择合适的字体大小
    adjusted_font_height = int(font_width * aspect_ratio)
    font = ImageFont.load_default()

    # 创建新的调整尺寸的图像
    adjusted_img_width = new_width * font_width
    adjusted_img_height = new_height * adjusted_font_height
    output_img = Image.new('L', (adjusted_img_width, adjusted_img_height), color=255)
    draw = ImageDraw.Draw(output_img)

    for i, line in enumerate(textual_symbol_img_list):
        for j, symbol in enumerate(line):
            # 我们列表中的最后一个符号表示最浅的阴影
            if symbol != TEXTUAL_SYMBOLS[-1]:
                draw.text((j*font_width, i*adjusted_font_height), symbol, font=font, fill=0)

    # 保存调整后的图像
    output_img.save(output_path)

if __name__ == "__main__":
    # 修改此行以适应您的输入图像名称
    input_image_path = r"C:\Users\howen\Desktop\微信图片_20230812221029.jpg"
    # 这将把图像保存到工作目录
    output_image_path = "output_image.jpg"
    convert_image_to_textual_symbols(input_image_path, output_image_path)
    print(f"Converted image saved to {output_image_path}")
