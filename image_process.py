from PIL import Image
import os

def process_image(img_path, num):
    """ 处理图片 """
    # ...
    # 设置大图中每个小图的大小
    size = (1920, 1920)

    def get_image_paths(path):
        """ 返回路径下所有图片的完整路径 """
        for file_name in os.listdir(path):
            ext = os.path.splitext(file_name)[1].lower()
            if ext in ('.jpg', '.png', '.tif'):
                yield os.path.join(path, file_name)

    # 获取目标文件夹中所有图片路径
    path = img_path
    col_num = int(num)

    imgs = sorted(get_image_paths(path))

    # 计算大图的大小
    rows = (len(imgs) - 1) // col_num + 1
    result_size = (size[0] * col_num, size[1] * rows)

    # 创建空白大图
    result_img = Image.new('RGB', result_size, 'white')

    # 拼接图片
    for i, img_path in enumerate(imgs):
        with Image.open(img_path).copy() as img:
            img.thumbnail(size)
            x = (i % col_num) * size[0]
            y = (i // col_num) * size[1]
            if img.size[0] > img.size[1]:
                offset = ((size[0] - img.size[0]) // 2, (size[1] - img.size[1]) // 2)
            else:
                offset = ((size[0] - img.size[0]) // 2, 0)
            result_img.paste(img, (x + offset[0], y + offset[1]))

    # 保存拼接后的大图片
    # result_img.save(os.path.join(path, 'res2.jpg'))
    return result_img


