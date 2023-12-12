import tkinter as tk
import os
import re
import requests
import aiohttp
import asyncio
from bs4 import BeautifulSoup


def sanitize_filename(filename):
    """
    清理文件名以确保它们是有效的文件夹名称。
    """
    return re.sub(r'[\\/*?:"<>|]', '', filename)


async def extract_image_info(keyword):
    print("嘿嘿哈哈")
    url = "https://www.vcg.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    search_form = soup.find('form', {'id': 'search_form'})
    if search_form is None:
        print("未找到搜索表单")
        # 此处应继续你的代码逻辑，例如从表单中获取数据等操作
    filled_form = search_form.hidden_fields()
    filled_form.append(('keyword', keyword))
    filled_form.append(('submit', '极速下载图片'))  # 这个字段是提交按钮的名称，根据实际情况可能会有所不同

    response = requests.post(url, data=filled_form)
    soup = BeautifulSoup(response.text, 'html.parser')

    image_info_list = []
    img_wrappers = soup.find_all('div', class_='imgWaper')
    for img_wrapper in img_wrappers:
        title = img_wrapper.get('title')
        img_element = img_wrapper.find('img')
        src = img_element.get('data-src')
        image_info_list.append({'title': title, 'src': src})

        # 创建关键词对应的文件夹
    folder_name = sanitize_filename(keyword)
    os.makedirs(folder_name, exist_ok=True)

    print("成功获取到图片信息！")
    for info in image_info_list:
        print(f"标题: {info['title']}, 链接: {info['src']}")
    print("----------正在下载图片中，预计15~30s内完成，请耐心等待-----------")

    # 下载图片并保存到文件夹
    async with aiohttp.ClientSession() as session:
        for index, info in enumerate(image_info_list):
            async with session.get(f"http:{info['src']}") as resp:
                if resp.status == 200:
                    image_data = await resp.read()
                    file_name = f"{folder_name}/{sanitize_filename(info['title'])}.jpg"
                    with open(file_name, "wb") as f:
                        f.write(image_data)
    # ...
    return "成功获取图片信息"


window = tk.Tk()
window.title("Memory图片下载器")
window.geometry("300x200")

keyword_label = tk.Label(window, text="关键词:")
keyword_label.pack(pady=10)
keyword_entry = tk.Entry(window)
keyword_entry.pack(pady=10)

execute_button = tk.Button(window, text="极速下载图片",
                           command=lambda: asyncio.run(extract_image_info(keyword_entry.get())))
execute_button.pack(pady=20)

print("欢迎使用 Memory 图片下载器！")
print("作者: @Memory")
print("""  
 *  
 (  `  
 )\))(    (    )       (   (  
((_)()\  ))\  (     (  )(  )\ )  
(_()((_)/((_) )\  ' )\(()\(()/(  
|  \/  (_)) _((_)) ((_)((_))(_))  
| |\/| / -_) '  \() _ \ '_| || |  
|_|  |_\___|_|_|_|\___/_|  \_, |  
                           |__/  
""")
print("----------------------------------------------------------------")
print("输入关键词，即可极速下载100+张相关图片")
print('点击 "极速下载图片" 按钮后，可能会出现短暂卡死，不要惊慌，属于正常现象')
print("请注意，下载图片需要花费巨额流量，不要轻易在非Wifi环境下使用！")
print("----------------------------------------------------------------")
print("")
# 运行窗口主循环
window.mainloop()
