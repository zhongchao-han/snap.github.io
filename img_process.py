from PIL import Image
import os

def resize_image_maintain_aspect_ratio(image_path, output_path, max_dimension=800):
    """
    将图片大小调整为最大边长为指定像素，并保持图片比例不变。

    Args:
        image_path (str): 输入图片的路径。
        output_path (str): 输出图片的保存路径。
        max_dimension (int): 调整后图片的最大边长（宽度或高度）像素值。
    """
    try:
        with Image.open(image_path) as img:
            original_width, original_height = img.size

            # 计算缩放比例
            if original_width > original_height:
                # 宽度是长边
                ratio = max_dimension / original_width
            else:
                # 高度是长边或图片是正方形
                ratio = max_dimension / original_height

            new_width = int(original_width * ratio)
            new_height = int(original_height * ratio)

            # 使用 ANTIALIAS 滤波器进行高质量缩放
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

            # 确保输出目录存在
            output_dir = os.path.dirname(output_path)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)

            resized_img.save(output_path)
            print(f"图片已成功调整大小并保存到：{output_path}")
            print(f"原始尺寸：{original_width}x{original_height}")
            print(f"新尺寸：{new_width}x{new_height}")

    except FileNotFoundError:
        print(f"错误：文件未找到，请检查路径：{image_path}")
    except Exception as e:
        print(f"处理图片时发生错误：{e}")

# --- 使用示例 ---
if __name__ == "__main__":
    # 假设你的图片文件名为 'example.jpg' 并且在当前目录下
    # 你可以修改为你的图片路径
    input_image = 'Gemini_Generated_Image_jy8pj9jy8pj9jy8p.png'
    output_image = 'ad_image_800_1.png'

    # 创建一个示例图片文件用于测试 (如果 'your_image.jpg' 不存在)
    if not os.path.exists(input_image):
        print(f"未找到示例图片 '{input_image}'，正在创建一个虚拟图片用于测试...")
        try:
            # 创建一个简单的白色图片作为占位符
            dummy_img = Image.new('RGB', (1920, 1080), color = 'white') # 示例尺寸
            dummy_img.save(input_image)
            print(f"已创建虚拟图片 '{input_image}'。")
        except Exception as e:
            print(f"创建虚拟图片失败：{e}")
            print("请确保你有一个名为 'your_image.jpg' 的图片文件在脚本运行目录下，或修改 input_image 变量为你的图片路径。")
            exit() # 如果无法创建虚拟图片，则退出

    resize_image_maintain_aspect_ratio(input_image, output_image, max_dimension=800)

    # 另一个例子：如果图片是正方形或高度更长
    # input_image_2 = 'your_image_square.png'
    # output_image_2 = 'resized_image_800_square.png'
    # if not os.path.exists(input_image_2):
    #     print(f"未找到示例图片 '{input_image_2}'，正在创建一个虚拟图片用于测试...")
    #     try:
    #         dummy_img_2 = Image.new('RGB', (600, 1200), color = 'blue')
    #         dummy_img_2.save(input_image_2)
    #         print(f"已创建虚拟图片 '{input_image_2}'。")
    #     except Exception as e:
    #         print(f"创建虚拟图片失败：{e}")
    # resize_image_maintain_aspect_ratio(input_image_2, output_image_2, max_dimension=800)