import socket
import psutil
from tkinter import Tk, Button, Text


class HostInfo:
    def __init__(self):
        self.root = Tk()
        self.root.title("本机信息")
        self.text = Text(self.root)
        self.text.pack()
        self.button = Button(self.root, text="获取本机信息", command=self.create_window)
        self.button.pack()

    def create_window(self):
        # 获取本机主机名
        hostname = socket.gethostname()
        print("本机主机名：", hostname)

        # 获取本机 IP 地址
        ip_address = socket.gethostbyname(socket.gethostname())
        print("本机 IP 地址：", ip_address)

        # 获取本机域名
        domain = socket.getfqdn()
        print("本机域名：", domain)

        # 获取本机上传下载速度
        net_io_counters = psutil.net_io_counters(pernic=True)
        for interface, counters in net_io_counters.items():
            if interface == 'WLAN':
                print(f"{interface}:")
                print(f"  上传速度： {counters.bytes_sent / 1024:.2f} KB/s")
                print(f"  下载=度： {counters.bytes_recv / 1024:.2f} KB/s")

            if interface == '蓝牙网络连接':
                print(f"{interface}:")
                print(f"  上传速度： {counters.bytes_sent / 1024:.2f} KB/s")
                print(f"  下载速度： {counters.bytes_recv / 1024:.2f} KB/s")

        # 将本机信息显示在文本框中
        self.text.delete(1.0, "end")
        self.text.insert("insert", f"本机主机名：{hostname}")
        self.text.insert("insert", f"本机 IP 地址：{ip_address}")
        self.text.insert("insert", f"本机域名：{domain}")
        self.text.insert("insert", "本机上传下载速度：")
        for interface, counters in net_io_counters.items():
            if interface == 'WLAN':
                self.text.insert("insert", f"{interface}:")
                self.text.insert("insert", f"  上传速度： {counters.bytes_sent / 1024:.2f} KB/s")
                self.text.insert("insert", f"  下载=度： {counters.bytes_recv / 1024:.2f} KB/s")

            if interface == '蓝牙网络连接':
                self.text.insert("insert", f"{interface}:")
                self.text.insert("insert", f"  上传速度： {counters.bytes_sent / 1024:.2f} KB/s")
                self.text.insert("insert", f"  下载速度： {counters.bytes_recv / 1024:.2f} KB/s")

    def run(self):
        self.root.mainloop()


