import requests

# 打开repos.txt文件
with open("repos.txt", "r") as f:
    # 逐行读取文件内容
    for url in f:
        # 去掉换行符
        url = url.strip()
        # 发送HEAD请求，获取响应状态码
        status = requests.head(url).status_code
        # 打印结果
        print(f"|  {url} |  {status} |")

