import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
# window.geometry("300x225")
window.title("开始菜单")

# 加载背景图片
image = Image.open("D:\\Project\\星球项目\\MemoryTools\\imgs\\mountain2.jpg")
bg_image = ImageTk.PhotoImage(image)

# 创建标签并设置背景图片
bg_label = tk.Label(window, image=bg_image)
bg_label.pack(fill=tk.BOTH, expand=True)

window.mainloop()
