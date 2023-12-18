import tkinter as tk
import tkinter.filedialog as filedialog


# 简易笔记本
class MemoryNotepad:
    def __init__(self):
        self.window = None
        # 左侧操作区
        self.operate_frame = None
        # 打开按钮
        self.btn_open = None
        # 另存为按钮
        self.btn_save_as = None
        # 统计字数按钮
        self.btn_count = None
        # 文字编辑区
        self.txt_edit = None
        # 初始化字符数
        self.var_lbl = None
        # 字符数标签
        self.lbl = None

    # 打开本地文件
    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )

        if not file_path:
            self.window.title("无标题 - 记事本")
            return

        self.txt_edit.delete("1.0", tk.END)

        with open(file_path, mode="r", encoding="utf-8") as input_file:
            self.txt_edit.insert(tk.END,
                                 input_file.read()
                                 )
        self.window.title(f"{file_path} - 记事本")

    # 保存文件到本地
    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not file_path:
            return

        with open(file_path, mode="w", encoding="utf-8") as output_file:
            output_file.write(self.txt_edit.get("1.0", tk.END))

        self.window.title(f"{file_path} - 记事本")

    # 统计字符数量
    def count_chars_in_text(self):
        text = self.txt_edit.get("1.0", tk.END)  # 获取 Text 组件中的所有文本
        char_count = len(text) - 1  # 计算文本的长度

        print(f"字符数: {char_count}")
        self.var_lbl.set(f"字符数: {char_count}")  # 显示文本

    # 初始化 MemoryNotepad 窗口
    def init(self):
        self.window = tk.Tk()
        self.window.title("Memory Notepad")

        # 左侧操作区
        self.operate_frame = tk.Frame(master=self.window, bd=2)
        self.operate_frame.grid(row=0, column=0, sticky="ns")

        # 窗口大小不可变
        self.window.rowconfigure(0, minsize=100, weight=1)
        self.window.columnconfigure(1, minsize=100, weight=1)

        # 打开按钮
        self.btn_open = tk.Button(master=self.operate_frame, text="打开", command=self.open_file)
        self.btn_open.grid(row=0, column=0, padx=5, pady=5)

        # 另存为按钮
        self.btn_save_as = tk.Button(master=self.operate_frame, text="另存", command=self.save_as_file)
        self.btn_save_as.grid(row=1, column=0, sticky="ew", )

        # 统计字数按钮
        self.btn_count = tk.Button(master=self.window, text="统计字数", command=self.count_chars_in_text)
        self.btn_count.grid(row=1, column=1, sticky="ew")

        # 文字编辑区
        self.txt_edit = tk.Text(master=self.window)
        self.txt_edit.grid(row=0, column=1, sticky="nsew")

        # 初始化字符数
        self.var_lbl = tk.StringVar()
        self.var_lbl.set("")  # 初始化一个空字符串

        # 字符数标签
        self.lbl = tk.Label(master=self.btn_count, textvariable=self.var_lbl)
        self.lbl.grid(row=1, column=1, sticky="ew")

        # 监听文本内容改变
        self.txt_edit.config(font=("Arial", 12), undo=True, wrap="word")
        self.txt_edit.bind("<<Modified>>", self.count_chars_in_text)  # 当文本内容改变时触发事件并调用count_chars_in_text函数

        print("欢迎使用 Memory Notepad 笔记本软件")
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
        print("您可以用它来编辑文本文件，也可以快捷地统计文本字数")
        print("新的功能还在逐步开发完善中，敬请期待~")
        print("您不需要理会这个窗口，祝您使用愉快")

        # 生成窗口
        self.window.mainloop()

