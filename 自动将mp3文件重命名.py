import os
import re

def save_html_filenames(folder_path, output_list):
    # 遍历文件夹中的所有文件
    files = os.listdir(folder_path)
    # 对文件名进行排序
    files.sort(key=lambda x: int(re.findall(r'\d+', os.path.splitext(x)[0])[0]) if re.findall(r'\d+', os.path.splitext(x)[0]) else 0)
    for file in files:
        # 获取文件的完整路径
        file_path = os.path.join(folder_path, file)
        
        # 判断是否为HTML文件
        if file.endswith('.html'):
            # 获取文件名（不包括扩展名）
            file_name = os.path.splitext(file)[0]
            
            # 将文件名添加到输出列表中
            output_list.append(file_name)

# 调用函数，传入文件夹路径和输出列表
current_directory = os.getcwd()
output_names = []
save_html_filenames(current_directory, output_names)

# 遍历文件夹中的所有mp3文件
files = os.listdir(current_directory)
mp3_files = [file for file in files if file.endswith('.mp3')]
mp3_files.sort(key=lambda x: int(re.findall(r'\d+', os.path.splitext(x)[0])[0]) if re.findall(r'\d+', os.path.splitext(x)[0]) else 0)

for mp3_file in mp3_files:
    # 根据output_names中的文本对mp3文件进行重命名
    new_name = output_names.pop(0).strip() + '.mp3'
    os.rename(mp3_file, new_name)
