# mi_shop

### 项目介绍

小米商城闪购辅助神器，请勿用于不良用途 :smirk:

有什么东西看这里 https://www.mi.com/seckill/

### 使用教程
> 推荐在云服务器上运行，本地机器对网络延迟有信心也可以

- 依赖：Python3.6x， window谷歌浏览器


1. git clone https://github.com/Mengjianhua-c/mi_shangou.git
2. pip install -r requirements.txt
3. 配置浏览器，自动登录小米官网
    - 手动登录一次小米官网，并且勾选‘这是我的私人设备，下次登录无需认证’
    - 修改settings CHROME_OPTIONS_PATH成自己电脑的
    - 执行 python test.py, 确认脚本是否可以成功登录并获取cookies
#### 4.1 本地运行
> 适合本地网络延迟低，或云服务器是window的
1. 执行 python shangou.py
根据提示操作

#### 4.2 服务端执行

1. 配置好谷歌浏览器登录的客户端， 执行 python loop_web_cookies.py 等待任务

2. 服务端执行 python3 ser_shangou.py



### 注意事项
- 重要提示： **本工具仅用于测试学习交流使用，请勿用于不良用途(不要当黄牛)**
- 使用服务端执行的时候需要将cookies信息转存到服务器上，所以你的cookies信息有可能存在泄露风险，谨慎使用
- 不要用一个账户连续抢多次，亲测抢了三次账户就被屏蔽了
- 新注册的账户是没有抢购资格的，所以不要白费力气了==
- 有疑先建issue
- 没了...

