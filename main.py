import json
import os
import re
import time

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkdns.v2 import *
from huaweicloudsdkdns.v2.region.dns_region import DnsRegion

if __name__ == '__main__':
    # 华为云AK
    ak = "<Your AK>"
    
    # 华为云SK
    sk = "<Your SK>"
    
    # 主域名
    domain = "domain.com"
    
    # 子域名
    recordset = "www"
    
    # IP地址
    ip = ["8.8.8.8"]
    
    #网卡信息 默认 wan 口
    result = os.popen("ifconfig pppoe-wan").read()
    
    if find := re.search(r"inet addr:(\d+\.\d+\.\d+\.\d+)", result):
        ip[0] = find.group(1)
        print(ip[0])
    else:
        print("NULL")
    
    # 记录类型 无需修改
    dtype = "A"
    
    credentials = BasicCredentials(ak, sk) \
    
    client = DnsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(DnsRegion.value_of("cn-north-4")) \
        .build()
    
    try:
        request = ListRecordSetsRequest()
        request.name = recordset + "." + domain + "."  # 域名
        request.type = "A"
        response1 = json.loads(str(client.list_record_sets(request)))
        try:
            request = UpdateRecordSetRequest()
            request.zone_id = response1['recordsets'][0]['zone_id']  # 域名ID
            request.recordset_id = response1['recordsets'][0]['id']  # 解析ID
            listRecordsbody = ip
            name = recordset + "." + domain + "."  # 域名
            request.body = UpdateRecordSetReq(
                records=listRecordsbody,
                ttl=1,  # ttl数值
                description = time.strftime('更新时间：%Y-%m-%d- %H:%M:%S'),
                type=dtype,  # 解析记录类型
                name=name  # 域名
            )
            response2 = client.update_record_set(request)
            print("success")
        except exceptions.ClientRequestException as e:
            print(e.status_code)
            print(e.request_id)
            print(e.error_code)
            print(e.error_msg)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
