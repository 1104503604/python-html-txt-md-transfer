import os
import shutil
from bs4 import BeautifulSoup

current_directory = os.getcwd()
file_path = current_directory
folder_path = current_directory

#把XHTML文件转换成HTML
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

#把HTM文件转换成HTML
def convert_xhtml_to_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('<!DOCTYPE html>', '')
    new_file_path = file_path.replace('.htm', '.html')
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.write(content)
    return new_file_path

for file_name in os.listdir(folder_path):
    if file_name.endswith('.htm'):
        file_path = os.path.join(folder_path, file_name)
        new_file_path = convert_xhtml_to_html(file_path)
        
# 把HTML文件转换成txt，并整理为一行
for filename in os.listdir(current_directory):
    if filename.endswith(".html"):
        file_path = os.path.join(current_directory, filename)
        output_file = os.path.splitext(filename)[0] + ".txt"
        output_path = os.path.join(current_directory, output_file)

        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")

        with open(output_path, "w", encoding="utf-8") as file:
            for paragraph in soup.find_all("p"):
                file.write(paragraph.text.replace('\n', ' '))

# 把中文标注符号修改为英文标注符号
def replace_chinese_punctuation(text):
    chinese_punctuation = "，。！？【】（）《》“”‘’；：—"
    english_punctuation = ",.!?[]()<>\"\"'';:-"
    for c, e in zip(chinese_punctuation, english_punctuation):
        text = text.replace(c, e)
        text = text.replace('. . .', '.')
        text = text.replace('…', '.')
        text = text.replace('...', '.')
    return text

# 内容排版
def process_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        if file.endswith(".txt"):
            with open(os.path.join(input_folder, file), "r", encoding="utf-8") as f:
                content = f.read()
            new_content = replace_chinese_punctuation(content)

            new_folder = output_folder

            #遇到文本中含有"."或";"或":"等情况则执行一次回车操作
            with open(os.path.join(new_folder, file), "w", encoding="utf-8") as f:
                for i, char in enumerate(new_content):
                    if char == '.' and (i + 1 >= len(new_content) or new_content[i + 1] != '"') and not (i + 1 < len(new_content) and new_content[i + 1].isdigit()):
                        f.write('.')
                        f.write('\n')
                    elif char == '"' and (i - 1 >= len(new_content) or new_content[i - 1] == '.'):
                        f.write('"')
                        f.write('\n')
                    elif char == '"' and (i - 1 >= len(new_content) or new_content[i - 1] == '?'):
                        f.write('"')
                        f.write('\n')
                    elif char == ':':
                        f.write(':')
                        f.write('\n')
                    elif char == ';':
                        f.write(';')
                        f.write('\n')
                    else:
                        f.write(char)

            # 去掉行前面的空格
            with open(os.path.join(new_folder, file), 'r', encoding="utf-8") as f:
                lines = f.readlines()

            with open(os.path.join(new_folder, file), 'w', encoding="utf-8") as f:
                for line in lines:
                    if line[0] == ' ':
                        line = line[1:]
                    f.write(line)
                    f.write('\n')
                      
if __name__ == "__main__":  
    input_folder = current_directory  
    output_folder = current_directory
    process_files(input_folder, output_folder)


#删除xhtml文件
for filename in os.listdir(folder_path):
    if filename.endswith(".xhtml"):
        file_path = os.path.join(folder_path, filename)
        os.remove(file_path)
#删除htm文件
for filename in os.listdir(folder_path):
    if filename.endswith(".htm"):
        file_path = os.path.join(folder_path, filename)
        os.remove(file_path)
