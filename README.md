# huaweicloud-ddns
华为云DDNS Python脚本，本人用在Openwrt，其他程序稍微修改一下获取网卡IP的方式就可以

# 必要库
```
pip install huaweicloudsdkall
```
具体可以参考 https://github.com/huaweicloud/huaweicloud-sdk-python-v3/blob/master/README_CN.md#%E4%BA%91%E6%9C%8D%E5%8A%A1%E9%9B%86%E5%90%88%E5%8C%85

# 配置文件
|  变量名称   | 实例 | 描述  |
|  ----  | ----  | ----  |
| ak | - | Access Key Id |
| sk | - |Secret Access Key |
| domain | hw.wcnmb.cn | DNS解析域名 |
| recordset | ip | 解析记录 |
填写以上配置后 更新的DDNS域名为 ip.hw.wcnmb.cn
获取公网IP的方式为本地网卡，默认为pppoe-wan

在openwrt安装Python3环境后，在计划任务添加
```
* * * * * python ddns.py >> /root/log/huaweicloud-ddns.log 2>&1
```
表示每分钟提交一次更新，可根据需要减少频率
