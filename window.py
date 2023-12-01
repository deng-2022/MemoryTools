import tkinter as tk
import datetime
import subprocess
import webbrowser


# 实时更新时间
def update_time(label, window):
    # 获取当前时间并格式化为字符串
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 更新Label的文本为当前时间
    label['text'] = current_time
    window.after(1000, lambda: update_time(label, window))  # 开始时调用一次update_time函数，之后每秒更新一次时间


# 创建新窗口
def open_window(window_name, root):
    # 创建新的窗口实例
    new_window = tk.Toplevel(root)
    new_window.title(window_name)
    new_window.geometry("400x300+500+250")

    # 在新窗口中添加标签或其他组件
    label = tk.Label(new_window, text=window_name, font=("Arial", 18))
    label.pack(pady=50)


# 打开可执行文件
def execute_executable():
    # 指定可执行文件的完整路径
    executable_path = "E:\Singal_Games\GoldMiner\GoldMiner.exe"
    # executable_path = "D:\Project\python\程序打包\界面编程\GoldMiner\GoldMiner.exe"

    # 执行可执行文件
    process = subprocess.Popen(executable_path)


def open_docs():
    webbrowser.open('https://deng-2022.gitee.io/vuepress-docs3/')


# 定义一个函数，用于创建新的窗口
def create_menu_window(root):
    menu_window = tk.Toplevel(root)  # 创建新的窗口实例
    menu_window.title("新窗口")  # 设置新窗口的标题
    menu_window.geometry("400x300+500+250")

    # 创建上层Frame
    top_frame = tk.Frame(menu_window)
    top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    time_label = tk.Label(top_frame, text="", font=("Arial", 10))  # 初始化时间标签
    time_label.pack(side=tk.TOP)  # 在窗口顶部添加时间标签

    # 创建按钮并设置事件处理程序
    button1 = tk.Button(top_frame, text="开发者文档", font=("Arial", 12), command=open_docs)
    button1.pack(side=tk.TOP, padx=10)

    # 创建下层Frame
    bottom_frame = tk.Frame(menu_window)
    bottom_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # 创建按钮并设置事件处理程序
    button1 = tk.Button(bottom_frame, text="划水摸鱼", font=("Arial", 12))
    button1.pack(side=tk.TOP, padx=10)
    button1.bind("<Button-1>", lambda event: open_window("划水摸鱼", menu_window))

    button3 = tk.Button(bottom_frame, text="高效工具", font=("Arial", 12))
    button3.pack(side=tk.TOP, padx=10)
    button3.bind("<Button-1>", lambda event: open_window("高效工具", menu_window))

    # 创建定时器，每隔1秒更新时间
    menu_window.after(1000, lambda: update_time(time_label, menu_window))  # 开始时调用一次update_time函数，之后每秒更新一次时间


# 初始化窗口
def init_window():
    # 创建主窗口
    root = tk.Tk()
    root.geometry("300x225")
    root.title("Memery Tools")

    # 创建上层Frame
    top_frame = tk.Frame(root)
    top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # 在上层Frame中添加一个标签
    label = tk.Label(top_frame, text="欢迎使用 Memery Tools！", font=("Arial", 14))
    label.pack(pady=50)

    # 创建下层Frame，并使用grid来管理它
    bottom_frame = tk.Frame(root)
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    # 在下层Frame中添加按钮
    button = tk.Button(bottom_frame, text="开始使用", font=("Arial", 10), command=lambda: create_menu_window(root))
    button.pack()

    # 调整窗口样式
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.resizable(True, True)

    # 运行窗口
    root.mainloop()


if __name__ == '__main__':
    init_window()
