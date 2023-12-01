# 一个简单的笔记本
import tkinter as tk
import tkinter.filedialog as filedialog


# 打开文件
def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Text files", "*.txt"),
            ("All files", "*.*")
        ]
    )

    if not file_path:
        window.title("无标题 - 记事本")
        return

    txt_edit.delete("1.0", tk.END)

    with open(
            file_path,
            mode="r",
            encoding="utf-8") as input_file:
        txt_edit.insert(
            tk.END,
            input_file.read()
        )
    window.title(f"{file_path} - 记事本")


# 另存为
def save_as_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("Text files", "*.txt"),
            ("All files", "*.*")
        ]
    )
    if not file_path:
        return
    with open(
            file_path,
            mode="w",
            encoding="utf-8") as output_file:
        output_file.write(txt_edit.get("1.0", tk.END))
    window.title(f"{file_path} - 记事本")


# 统计字数
def count_chars_in_text():
    text = txt_edit.get("1.0", tk.END)  # 获取 Text 组件中的所有文本
    char_count = len(text) - 1  # 计算文本的长度
    print(f"字符数: {char_count}")
    var_lbl.set(f"字符数: {char_count}")  # 显示文本


window = tk.Tk()
window.title("记事本")

window.rowconfigure(
    0,
    minsize=100,
    weight=1
)
window.columnconfigure(
    1,
    minsize=100,
    weight=1
)

# 左侧操作区
btn_frame = tk.Frame(
    master=window,
    bd=2
)
btn_frame.grid(
    row=0,
    column=0,
    sticky="ns"
)

# 打开文本文件
btn_open = tk.Button(
    master=btn_frame,
    text="打开",
    command=open_file
)
btn_open.grid(
    row=0,
    column=0,
    sticky="ew",
    padx=5,
    pady=5
)

# 另存为
btn_save_as = tk.Button(
    master=btn_frame,
    text="另存",
    command=save_as_file
)
btn_save_as.grid(
    row=1,
    column=0,
    sticky="ew",
)

# 统计字数
btn_count = tk.Button(
    master=window,
    text="统计字数",
    command=count_chars_in_text
)
btn_count.grid(row=1, column=1, sticky="ew")

# 字符数
var_lbl = tk.StringVar()
var_lbl.set("")  # 初始化一个空字符串

lbl = tk.Label(
    master=btn_count,
    textvariable=var_lbl
)

lbl.grid(row=1, column=1, sticky="ew")

# 读写区
txt_edit = tk.Text(master=window)
txt_edit.grid(
    row=0,
    column=1,
    sticky="nsew"
)

# 当文本内容改变时，调用count_chars_in_text函数
txt_edit.config(font=("Arial", 12), undo=True, wrap="word")
txt_edit.bind("<<Modified>>", count_chars_in_text)  # 当文本内容改变时触发事件并调用count_chars_in_text函数

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

window.mainloop()
