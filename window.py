import tkinter as tk
import datetime
import subprocess
import webbrowser

from MemoryNotepad import MemoryNotepad
from MemoryTranslator import MemoryTranslator
from MemoryWeather import MemoryWeather
from MemoryAIChat import AIChat


class MemoryTools:
    def __init__(self):
        # 创建主窗口
        self.window = tk.Tk()
        self.window.geometry("300x225")
        self.window.title("Memery Tools")

        # 创建上层Frame
        self.top_frame = tk.Frame(self.window)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # 在上层Frame中添加一个标签
        self.label = tk.Label(self.top_frame, text="欢迎使用 Memery Tools！", font=("Arial", 14))
        self.label.pack(pady=50)

        # 创建下层Frame，并使用grid来管理它
        self.bottom_frame = tk.Frame(self.window)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # 在下层Frame中添加按钮
        self.button = tk.Button(self.bottom_frame, text="开始使用", font=("Arial", 10),
                                command=lambda: self.create_menu_window(self.window))
        self.button.pack()

        # 调整窗口样式
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.resizable(True, True)

    # 实时更新时间
    def update_time(self, label, window):
        # 获取当前时间并格式化为字符串
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 更新Label的文本为当前时间
        label['text'] = current_time
        window.after(1000, lambda: self.update_time(label, window))  # 开始时调用一次update_time函数，之后每秒更新一次时间

    # 创建新窗口
    @staticmethod
    def open_window(window_name, root):
        # 创建新的窗口实例`
        new_window = tk.Toplevel(root)
        new_window.title(window_name)
        new_window.geometry("400x300+500+250")

        # 在新窗口中添加标签或其他组件
        label = tk.Label(new_window, text=window_name, font=("Arial", 18))
        label.pack(pady=50)

    # 打开可执行文件
    @staticmethod
    def execute_executable():
        # 指定可执行文件的完整路径
        executable_path = "E:\Singal_Games\GoldMiner\GoldMiner.exe"
        # executable_path = "D:\Project\python\程序打包\界面编程\GoldMiner\GoldMiner.exe"

        # 执行可执行文件
        process = subprocess.Popen(executable_path)

    @staticmethod
    def open_docs():
        webbrowser.open('https://deng-2022.gitee.io/vuepress-docs3/')

    # 定义一个函数，用于创建新的窗口
    def create_menu_window(self, root):
        menu_window = tk.Toplevel(root)  # 创建新的窗口实例
        # menu_window = tk.Tk()  # 创建新的窗口实例
        menu_window.title("新窗口")  # 设置新窗口的标题
        menu_window.geometry("400x300+500+250")

        # 创建上层Frame
        top_frame = tk.Frame(menu_window)
        # top_frame.grid()
        top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # 创建下层Frame
        bottom_frame = tk.Frame(menu_window)
        bottom_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        time_label = tk.Label(top_frame, text="", font=("Arial", 10))  # 初始化时间标签
        time_label.pack(side=tk.TOP)  # 在窗口顶部添加时间标签

        # # 创建按钮并设置事件处理程序
        button0 = tk.Button(top_frame, text="开发者文档", font=("Arial", 12), command=self.open_docs)
        button0.pack(side=tk.TOP, padx=10)

        # 创建按钮并设置事件处理程序
        memory_notepad = MemoryNotepad()
        button1 = tk.Button(top_frame, text="简易笔记本", font=("Arial", 12), command=lambda: memory_notepad.init())
        button1.pack(side=tk.LEFT, padx=10)

        memory_translator = MemoryTranslator()
        button2 = tk.Button(top_frame, text="英汉互译", font=("Arial", 12), command=lambda: memory_translator.init())
        button2.pack(side=tk.LEFT, padx=10)

        memory_weather = MemoryWeather()
        button3 = tk.Button(top_frame, text="天气查询", font=("Arial", 12), command=lambda: memory_weather.init())
        button3.pack(side=tk.LEFT, padx=10)

        ai_chat = AIChat()
        button4 = tk.Button(top_frame, text="AI对话", font=("Arial", 12), command=lambda: ai_chat.init())
        button4.pack(side=tk.LEFT, padx=10)

        button5 = tk.Button(bottom_frame, text="图片下载器", font=("Arial", 12))
        button5.pack(side=tk.LEFT, padx=10)
        button5.bind("<Button-1>", lambda event: self.open_window("图片下载器", menu_window))

        button6 = tk.Button(bottom_frame, text="本机信息", font=("Arial", 12))
        button6.pack(side=tk.LEFT, padx=10)
        button6.bind("<Button-1>", lambda event: self.open_window("本机信息", menu_window))

        # 创建定时器，每隔1秒更新时间
        menu_window.after(1000, lambda: self.update_time(time_label, menu_window))  # 开始时调用一次update_time函数，之后每秒更新一次时间

    # 初始化窗口
    def init_window(self):
        # 运行窗口
        self.window.mainloop()


if __name__ == '__main__':
    memory_tools = MemoryTools()
    memory_tools.init_window()
