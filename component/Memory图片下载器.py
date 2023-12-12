import tkinter as tk
import os
import re
import aiohttp
import asyncio
from playwright.async_api import async_playwright


def sanitize_filename(filename):
    """
    清理文件名以确保它们是有效的文件夹名称。
    """
    return re.sub(r'[\\/*?:"<>|]', '', filename)


async def extract_image_info(keyword):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        # 访问网页
        await page.goto("https://www.vcg.com/")

        # 输入关键字并点击搜索按钮
        await page.fill('input', keyword)
        await page.click('._3Kq4A')
        await asyncio.sleep(6)

        # 获取所有 .imgWaper 元素的标题和图片链接
        image_info_list = await page.evaluate('''() => {
            const imgWaperElements = document.querySelectorAll('.imgWaper');
            const infoList = [];
            imgWaperElements.forEach(element => {
                const title = element.getAttribute('title');
                const src = element.querySelector('img').getAttribute('data-src');
                infoList.push({title, src});
            });
            return infoList;
        }''')

        # 创建关键词对应的文件夹
        folder_name = sanitize_filename(keyword)
        os.makedirs(folder_name, exist_ok=True)

        # 输出标题和图片链接
        print("成功获取到图片信息！")
        for info in image_info_list:
            print(f"标题: {info['title']}, 链接: http:{info['src']}")
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

        await browser.close()

# 获取当前脚本所在的目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 设置 Playwright 可执行文件的路径
playwright_executable_path = os.path.join(script_dir, "node_modules", "playwright", "install-playwright")
# 设置输出目录
output_dir = os.path.join(script_dir, "dist")

# 使用 PyInstaller 打包时，将 Playwright 可执行文件复制到输出目录
os.environ["PLAYWRIGHT_BINARY"] = playwright_executable_path
os.environ["PW_CLIENT_BINARY"] = playwright_executable_path
os.environ["PW_CHROME_BINARY"] = playwright_executable_path
os.environ["PW_GECKODRIVER_BINARY"] = playwright_executable_path
os.environ["PW_STORAGE_DIR"] = output_dir


# 创建窗口的布局和组件
window = tk.Tk()
window.title("Memory图片下载器")
window.geometry("300x200")

# 创建关键词标签和输入框
keyword_label = tk.Label(window, text="关键词:")
keyword_label.pack(pady=10)
keyword_entry = tk.Entry(window)
keyword_entry.pack(pady=10)

# 创建执行按钮
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
