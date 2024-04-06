from bs4 import BeautifulSoup
import requests

url = "https://pvp.qq.com/cp/a20170829bbgxsm/index.html"

def remove_lines(filename, num_lines):
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        file.writelines(lines[num_lines:])

def add_blank_line_after_specific_line(filename, target_line):
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if line.strip() == target_line:
                file.write('\n')

if __name__ == "__main__":
    
    source = requests.get(url)
    source.encoding = "gbk"
    source = source.text

    # 创建 BeautifulSoup 对象
    soup = BeautifulSoup(source, 'html.parser')

    # 找到页面中所有的文本，并输出
    all_text = soup.get_text()

    length = len(all_text)

    all_text_1 = ""

    for i in range(1, length):
        if all_text[i] == "\n" and all_text[i - 1] == "\n":
            continue
        else:
            all_text_1 += all_text[i]

    with open("index.txt", "w") as f:
        f.write(all_text_1)

    remove_lines("index.txt", 4)
    add_blank_line_after_specific_line("index.txt", "查看版本详情")