import socket
import psutil
from tkinter import Tk, Button, Text


# 获取本机信息
class MemoryHostInfo:
    def __init__(self):
        self.root = None
        # 初始化对话框
        self.text = None
        # 初始化按钮
        self.button = None

    # 获取本机信息
    def create_window(self):
        # 获取本机主机名
        hostname = socket.gethostname()
        print("本机主机名：", hostname, "\n")

        # 获取本机 IP 地址
        ip_address = socket.gethostbyname(socket.gethostname())
        print("本机 IP 地址：", ip_address, "\n")

        # 获取本机域名
        domain = socket.getfqdn()
        print("本机域名：", domain, "\n")

        # 获取本机上传下载速度
        net_io_counters = psutil.net_io_counters(pernic=True)
        for interface, counters in net_io_counters.items():
            if interface == 'WLAN':
                print(f"{interface}:")
                print(f"  上传速度： {counters.bytes_sent / 1024:.2f} KB/s\n")
                print(f"  下载速度： {counters.bytes_recv / 1024:.2f} KB/s\n")

            if interface == '蓝牙网络连接':
                print(f"{interface}:")
                print(f"  上传速度： {counters.bytes_sent / 1024:.2f} KB/s\n")
                print(f"  下载速度： {counters.bytes_recv / 1024:.2f} KB/s\n")

        # 将本机信息显示在文本框中
        self.text.delete(1.0, "end")
        self.text.insert("insert", f"本机主机名：{hostname}\n\n")
        self.text.insert("insert", f"本机 IP 地址：{ip_address}\n\n")
        self.text.insert("insert", f"本机域名：{domain}\n\n")
        self.text.insert("insert", "本机上传下载速度：\n\n")
        for interface, counters in net_io_counters.items():
            if interface == 'WLAN':
                self.text.insert("insert", f"{interface}:\n")
                self.text.insert("insert", f"  上传速度： {counters.bytes_sent / 1024:.2f} KB/s\n")
                self.text.insert("insert", f"  下载速度： {counters.bytes_recv / 1024:.2f} KB/s\n\n")

            if interface == '蓝牙网络连接':
                self.text.insert("insert", f"{interface}:\n")
                self.text.insert("insert", f"  上传速度： {counters.bytes_sent / 1024:.2f} KB/s\n")
                self.text.insert("insert", f"  下载速度： {counters.bytes_recv / 1024:.2f} KB/s\n")

    # 初始化窗口
    def run(self):
        # 初始化窗口
        self.root = Tk()
        self.root.title("Memory HostInfo")
        # 对话框
        self.text = Text(self.root)
        self.text.pack()
        # 本机信息按钮
        self.button = Button(self.root, text="获取本机信息", command=self.create_window)
        self.button.pack()

        print("欢迎使用 Memory HostInfo 获取本机信息软件！")
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

        # 生成窗口
        self.root.mainloop()
