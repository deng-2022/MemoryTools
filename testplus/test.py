import tkinter as tk


def create_window():
    window = tk.Tk()  # 创建窗口
    window.title("我的窗口")  # 设置窗口标题
    window.geometry("300x200")  # 设置窗口大小

    # 添加一些组件，如标签，按钮等
    label = tk.Label(window, text="欢迎来到我的窗口！")
    label.pack()

    button = tk.Button(window, text="点击我")
    button.pack()

    # 启动主循环，显示窗口
    # window.mainloop()


class MemoryNotepad:
    def __init__(self):
        self.window1 = tk.Tk()
        self.window1.title("记事本")
        # self.window.mainloop()


class MemoryTools:
    def __init__(self):
        self.window2 = tk.Tk()
        self.window2.title("MemoryTools")

    def create_window(self):
        mn = MemoryNotepad()
        self.window2.mainloop()


if __name__ == '__main__':
    mt = MemoryTools()
    mt.create_window()
