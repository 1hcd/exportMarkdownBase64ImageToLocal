import re
import os
import base64
import chardet
import time

path = "E:\\" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
s = []

def extractBase64Images(md_file):
    with open(md_file, 'rb') as file:
        raw_data = file.read()
        encoding = chardet.detect(raw_data)['encoding']

    with open(md_file, 'r', encoding=encoding) as file:
        data = file.read()

    data = data.replace('`', '')

    img_pattern = re.compile(r'!\[([^\]]*)\](\(data:image\/(jpeg|gif|png);base64,([^\)]+)\))')
    images = img_pattern.findall(data)

    # 如果images文件夹不存在，创建它
    if not os.path.exists('images'):
        os.makedirs('images')

    for match in images:
        img_name, full_match, img_type, img_base64 = match

        # 处理不完整的base64编码
        missing_padding = len(img_base64) % 4
        if missing_padding:
            img_base64 += '='* (4 - missing_padding)

        t = int(round(time.time() * 1000))    #毫秒级时间戳

        # 转换并保存图片
        with open(f'images/{t}-{img_name}.{img_type}', 'wb') as img_file:
            img_file.write(base64.b64decode(img_base64))
    
        # 在原始数据中删除图片标记
        data = data.replace(full_match, '')

        # 将markdown文件中的图片引用修改为新的路径
        data = data.replace(f'![{img_name}]', f'![[images/{t}-{img_name}.{img_type}]]', 1)
        print(f"data: {data}")

        time.sleep(0.5)

    # 保存修改后的Markdown数据
    with open(md_file, 'w', encoding=encoding) as file:
        file.write(data)


def clearBlankLine(md_file):
    prefix = "nb-"
    target = prefix + md_file

    with open(md_file, 'rb') as file:
        raw_data = file.read()
        encoding = chardet.detect(raw_data)['encoding']

    with open(md_file, 'r', encoding=encoding) as src_file, \
        open(target, 'w', encoding=encoding) as tag_file:
        for line in src_file:
            if line.strip():  # 非空行
                tag_file.write(line)  # 保留原有换行符
            # 否则跳过空行

if __name__ == "__main__":
    with open("targets.txt", 'rb') as file:
        raw_data = file.read()
        encoding = chardet.detect(raw_data)['encoding']

    with open("targets.txt", 'r', encoding=encoding) as file:
        for mdFile in file.readlines():
            mdFile = mdFile.strip('\n')  #去掉列表中每一个元素的换行符
            if ".md" in mdFile:
                print(mdFile)
                extractBase64Images(mdFile)
                clearBlankLine(mdFile)

    

