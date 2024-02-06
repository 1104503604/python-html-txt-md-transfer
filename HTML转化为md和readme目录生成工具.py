import os
import re
from bs4 import BeautifulSoup

current_directory = os.getcwd()
folder_path = current_directory

def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        if re.match(r'^\d\.', filename):
            new_filename = '0' + filename
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            os.rename(old_file_path, new_file_path)

def convert_xhtml_to_html(file_path, extension):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('<!DOCTYPE html>', '')
    new_file_path = file_path.replace(extension, '.html')
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.write(content)
    return new_file_path

def get_html_files(folder_path):
    html_files = []
    for file in os.listdir(folder_path):
        if file.endswith(".html"):
            html_files.append(os.path.join(folder_path, file))
    return html_files

def save_text_to_md(html_file, md_file, counter, md_folder_path):
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text()
    lines = text.splitlines()
    lines = [line + "\n\n" for line in lines]
    text = "".join(lines)
    md_file = os.path.join(md_folder_path, "chapter" + str(counter).zfill(2) + ".md")
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(text)

def create_md_folder(folder_path):
    folder_name = os.path.basename(folder_path)
    md_folder_name = "book"
    md_folder_path = os.path.join(folder_path, md_folder_name)
    os.mkdir(md_folder_path)
    return md_folder_path

def main():
    folder_path = current_directory
    rename_files(folder_path)
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xhtml'):
            file_path = os.path.join(folder_path, file_name)
            new_file_path = convert_xhtml_to_html(file_path, '.xhtml')
        elif file_name.endswith('.htm'):
            file_path = os.path.join(folder_path, file_name)
            new_file_path = convert_xhtml_to_html(file_path, '.htm')
    html_files = get_html_files(folder_path)
    md_folder_path = create_md_folder(folder_path)
    counter = 1 # 初始化计数器
    for html_file in html_files:
        file_name = os.path.splitext(os.path.basename(html_file))[0]
        md_file = os.path.join(md_folder_path, file_name + ".md")
        save_text_to_md(html_file, md_file, counter, md_folder_path) # 传入md_folder_path参数
        counter += 1 # 递增计数器

def find_md_files(folder_path):
    md_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.html'):
                md_files.append(os.path.join(root, file))
    return md_files

def write_to_txt(md_files, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for file in md_files:
            f.write(os.path.basename(file) + '\n')

folder_path = current_directory
output_file = 'readme目录.txt'  # 输出的txt文件名

md_files = find_md_files(folder_path)
write_to_txt(md_files, output_file)


with open(output_file, 'r') as f:
    lines = f.readlines()

with open('README.md', 'w') as f:
    for line in lines:
        match = re.search(r'\d+', line)
        if match:
            number = match.group()
            line = line.replace('-', ' ')
            line = line.replace('.html', '')
            f.write('- [{}](./book/chapter{}.md)\n'.format(line.strip(), number))


if __name__ == "__main__":
    main()
