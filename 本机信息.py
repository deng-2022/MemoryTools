import socket
import psutil


class HostInfo:

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
            if (interface == 'WLAN'):
                print(f"{interface}:")
                print(f"  上传速度： {counters.bytes_sent / 1024:.2f} KB/s")
                print(f"  下载=度： {counters.bytes_recv / 1024:.2f} KB/s")
            if (interface == '蓝牙网络连接'):
                print(f"{interface}:")
                print(f"  上传速度： {counters.bytes_sent / 1024:.2f} KB/s")
                print(f"  下载速度： {counters.bytes_recv / 1024:.2f} KB/s")


if __name__ == '__main__':
    host_info = HostInfo()
    host_info.create_window()
