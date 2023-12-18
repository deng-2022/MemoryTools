import tkinter as tk
from translate import Translator


# 英汉互译
class MemoryTranslator:
    def __init__(self):
        self.root = None
        # 左侧操作区
        self.frame_left = None
        # 右侧操作区
        self.frame_right = None
        # 按钮区
        self.frame_button = None
        # 左侧提示
        self.left_label = None
        # 左侧文本框
        self.left_textbox = None
        # 右侧提示
        self.right_label = None
        # 右侧文本框
        self.right_textbox = None
        # 英译汉按钮
        self.en_to_zh = None
        # 汉译英按钮
        self.zh_to_en = None

    # 执行翻译文本
    @staticmethod
    def translate_text(text, from_lang, target_lang):
        translator = Translator(from_lang=from_lang, to_lang=target_lang)

        # 执行文本翻译
        result = translator.translate(text)
        return result

    # 监听英译汉按钮点击
    def en_to_zh_button_click(self):
        # 获取左侧文本框中的文本内容
        left_text = self.left_textbox.get('1.0', tk.END)

        # 执行英译汉翻译
        translated_text = self.translate_text(left_text, 'en', 'zh')
        print(f"英译汉结果: {translated_text}")

        # 实时更新右侧文本框中的内容(英译汉结果)
        self.right_textbox.delete('1.0', tk.END)
        self.right_textbox.insert(tk.END, translated_text)

    # 监听汉译英按钮点击
    def zh_to_en_button_click(self):
        # 获取右侧文本框中的文本内容
        right_text = self.right_textbox.get('1.0', tk.END)

        # 执行汉译英翻译
        translated_text = self.translate_text(right_text, 'zh', 'en')
        print(f"汉译英结果: {translated_text}")

        # 实时更新右侧文本框中的的内容(汉译英结果)
        self.left_textbox.delete('1.0', tk.END)
        self.left_textbox.insert(tk.END, translated_text)

    # 初始化窗口
    def init(self):
        self.root = tk.Tk()

        # 窗口属性设置
        self.root.title("Memory Translator")
        self.root.geometry("600x300")

        # 左侧操作区
        self.frame_left = tk.Frame(self.root)
        self.frame_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 右侧操作区
        self.frame_right = tk.Frame(self.root)
        self.frame_right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 按钮区
        self.frame_button = tk.Frame(self.root)
        self.frame_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 左侧提示
        self.left_label = tk.Label(self.frame_left, text="在这里输入英文")
        self.left_label.pack(side=tk.TOP)

        # 左侧文本框
        self.left_textbox = tk.Text(self.frame_left, width=30, height=10)
        self.left_textbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)

        # 右侧提示
        self.right_label = tk.Label(self.frame_right, text="在这里输入中文")
        self.right_label.pack(side=tk.TOP)

        # 右侧文本框
        self.right_textbox = tk.Text(self.frame_right, width=30, height=10)
        self.right_textbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)

        # 英译汉按钮
        self.en_to_zh = tk.Button(self.frame_button, text="英译汉", command=self.en_to_zh_button_click)
        self.en_to_zh.pack(pady=70)

        # 汉译英按钮
        self.zh_to_en = tk.Button(self.frame_button, text="汉译英", command=self.zh_to_en_button_click)
        self.zh_to_en.pack()

        print("欢迎使用 Memory Translator 翻译软件！")
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
        print("这是一个简单且好用的翻译软件，祝您使用愉快！")

        # 生成窗口
        self.root.mainloop()
