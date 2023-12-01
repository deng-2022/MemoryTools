import tkinter as tk
from translate import Translator


# 翻译文本
def translate_text(text, from_lang, target_lang):
    """Translate the text to Chinese using translate library."""
    translator = Translator(from_lang=from_lang, to_lang=target_lang)
    result = translator.translate(text)
    return result


# 监听按钮点击
def en_to_zh_button_click():
    """Handle the button click event."""
    # Get the text from the left text box
    left_text = left_textbox.get('1.0', tk.END)
    # Translate the text to Chinese
    translated_text = translate_text(left_text, 'en', 'zh')
    print(f"英译汉结果: {translated_text}")
    # Print the translated text in the right text box
    right_textbox.delete('1.0', tk.END)
    right_textbox.insert(tk.END, translated_text)


def zh_to_en_button_click():
    """Handle the reverse button click event."""
    # Get the text from the right text box
    right_text = right_textbox.get('1.0', tk.END)
    # Translate the text from Chinese
    translated_text = translate_text(right_text, 'zh', 'en')
    print(f"汉译英结果: {translated_text}")

    # Print the translated text in the left text box
    left_textbox.delete('1.0', tk.END)
    left_textbox.insert(tk.END, translated_text)


# Create the main window with two text boxes and a button
root = tk.Tk()
root.title("Translation App")
root.geometry("600x300")

frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

frame_right = tk.Frame(root)
frame_right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

frame_button = tk.Frame(root)
frame_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 创建左边的文本框和标签
left_label = tk.Label(frame_left, text="在这里输入英文")
left_label.pack(side=tk.TOP)
left_textbox = tk.Text(frame_left, width=30, height=10)
left_textbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)

# 创建右边的文本框和标签
right_label = tk.Label(frame_right, text="在这里输入中文")
right_label.pack(side=tk.TOP)
right_textbox = tk.Text(frame_right, width=30, height=10)
right_textbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)

# Create the button and bind the on_button_click function to it
en_to_zh = tk.Button(frame_button, text="英译汉", command=en_to_zh_button_click)
en_to_zh.pack(pady=70)

# Create the reverse button and bind the on_reverse_button_click function to it
zh_to_en = tk.Button(frame_button, text="汉译英", command=zh_to_en_button_click)
zh_to_en.pack()

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

# Start the main event loop of the application
root.mainloop()
