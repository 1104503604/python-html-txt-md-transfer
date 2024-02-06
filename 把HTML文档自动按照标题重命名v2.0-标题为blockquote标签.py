import os
from bs4 import BeautifulSoup

current_directory = os.getcwd()
folder_path = current_directory
a = 1

def convert_xhtml_to_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('<!DOCTYPE html>', '')
    new_file_path = file_path.replace('.xhtml', '.html')
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.write(content)
    return new_file_path

for file_name in os.listdir(folder_path):
    if file_name.endswith('.xhtml'):
        file_path = os.path.join(folder_path, file_name)
        new_file_path = convert_xhtml_to_html(file_path)

def clean_filename(filename):
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        filename = filename.replace(char, '')
    return filename

for file_name in os.listdir(folder_path):
    if file_name.endswith('.html'):
        file_path = os.path.join(folder_path, file_name)
        
        # 读取HTML文件内容
        with open(file_path, 'r', encoding='utf-8') as html_file:
            html_content = html_file.read()
        
        # 使用BeautifulSoup解析HTML文档
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 提取所需的文本
        blockquote_tags = soup.find_all(['blockquote'])[:2]
        new_file_name = ''
        for blockquote_tag in blockquote_tags:
            new_file_name += blockquote_tag.text.strip().lower() + '-'
        
        # 如果首个词不是数字，则在前面添加一个数字a
        if new_file_name.split():
            first_word = new_file_name.split()[0]
            if not first_word[0].isdigit():
                new_file_name = str(a) + '.' + new_file_name
                a += 1
        else:
            # 处理空列表的情况，例如设置 first_word 为默认值或者抛出异常
            pass
        
        # 重命名文件
        new_file_path = os.path.join(folder_path, clean_filename(new_file_name) + '.html')
        while os.path.exists(new_file_path):
            new_file_name += '1'
            new_file_path = os.path.join(folder_path, clean_filename(new_file_name) + '.html')
        os.rename(file_path, new_file_path)

#删除xhtml文件
for filename in os.listdir(folder_path):
    if filename.endswith(".xhtml") or filename.endswith(".htm"):
        file_path = os.path.join(folder_path, filename)
        os.remove(file_path)
