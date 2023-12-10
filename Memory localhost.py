from speedtest_cli import Speedtest

# 实例化测试类
spt = Speedtest()

# 获取最快的服务器
spt.get_best_server()

print('=============== 开始测试下载速度 ================')

# 测试下载速度，单位是Byte
downSp = spt.download()

# 打印结果，转换为Mb
print(f'=============== 下载速度是：{downSp /1024/1024:.2f} Mb/s ================')

print('=============== 开始测试上传速度 ================')

# 测试上传速度，单位是Byte
upSp = spt.upload()

print(f'=============== 上传速度是：{upSp /1024/1024:.2f} Mb/s ================')
