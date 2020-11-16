import os
from PIL import Image


def search_image(path):
    """
    在指定路径下搜索以'jpg', 'jpeg', 'png'后缀的图片名称
    :param path:
    :return:
    """
    ext = ['jpg', 'jpeg', 'png']
    files = os.listdir(path)
    # print(files)
    image_files = list(filter(lambda x: x.split('.')[-1] in ext, files))
    return image_files


def process_image(path, filename, m_width=490, m_height=490):
    """
    根据规定的长宽，调节实际图片的长宽
    :param filename:
    :param m_width:
    :param m_height:
    :return:
    """
    image = Image.open(path+filename)
    w, h = image.size
    # 图片尺寸长宽任何一个不超过规定的长宽，不做处理
    if w <= m_width and h <= m_height:
        print(filename, w, h)
        print(filename, 'is OK~')
        return
    print(filename, w, h)
    # 以规定的长宽缩短实际的长宽规则：
    # 宽比例大于长比例时，以宽比例做基准，也就是实际宽，调节到规定的宽；实际长，根据宽的调整比例去调节。
    # 长比例大于宽比例时，以长比例做基准，也就是实际长，调节到规定的长；实际宽按照相同比例调整。
    if 1.0*w/m_width > 1.0*h/m_height:
        scale = 1.0*w/m_width
        new_width = int(w / scale)
        new_height = int(h / scale)
        new_im = image.resize((new_width, new_height), Image.ANTIALIAS)
    else:
        scale = 1.0*h/m_height
        new_width = int(w / scale)
        new_height = int(h / scale)
        new_im = image.resize((new_width, new_height), Image.ANTIALIAS)
    # 保存调整后的图片
    new_im.save("D:/Web/websites/html/img/"+filename)
    new_im.close()


if __name__ == '__main__':
    path = "D:/Web/websites/html/img/pre_img/11_16_1/"
    file_names = search_image(path)
    for file in file_names:
        process_image(path, file)
